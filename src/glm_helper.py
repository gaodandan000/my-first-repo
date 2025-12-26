#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GLM Helper - 智谱AI GLM助手工具
GLM Helper - Zhipu AI GLM Assistant Tool
"""

import os
import yaml
from pathlib import Path
from zhipuai import ZhipuAI


class GLMHelper:
    """GLM助手类，封装常用的GLM API操作"""

    def __init__(self, config_path=None):
        """
        初始化GLM助手

        Args:
            config_path: 配置文件路径，默认使用 config/glm_config.yaml
        """
        self.config = self._load_config(config_path)
        self.client = self._init_client()

    def _load_config(self, config_path=None):
        """加载配置文件"""
        if config_path is None:
            # 默认配置文件路径
            repo_root = Path(__file__).parent.parent
            config_path = repo_root / "config" / "glm_config.yaml"

        if not config_path.exists():
            return self._default_config()

        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        return config

    def _default_config(self):
        """返回默认配置"""
        return {
            'api': {
                'timeout': 60
            },
            'model': {
                'name': 'glm-4',
                'temperature': 0.7,
                'top_p': 0.9,
                'max_tokens': 2048
            }
        }

    def _init_client(self):
        """初始化ZhipuAI客户端"""
        api_key = os.getenv("GLM_API_KEY")
        if not api_key:
            raise ValueError("请设置环境变量 GLM_API_KEY")

        return ZhipuAI(api_key=api_key)

    def chat(self, prompt, model=None, **kwargs):
        """
        发送聊天请求

        Args:
            prompt: 用户提示词
            model: 模型名称，默认使用配置文件中的模型
            **kwargs: 其他参数（temperature, top_p, max_tokens等）

        Returns:
            模型响应内容
        """
        model = model or self.config['model']['name']
        temperature = kwargs.get('temperature', self.config['model']['temperature'])
        top_p = kwargs.get('top_p', self.config['model']['top_p'])
        max_tokens = kwargs.get('max_tokens', self.config['model']['max_tokens'])

        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    def generate_code(self, description, language="Python"):
        """
        生成代码

        Args:
            description: 代码功能描述
            language: 编程语言

        Returns:
            生成的代码
        """
        prompt = f"""
请用{language}生成代码实现以下功能：

{description}

要求：
1. 代码清晰易读
2. 包含必要的注释
3. 遵循最佳实践
4. 包含错误处理
"""
        return self.chat(prompt)

    def review_code(self, code, language="Python"):
        """
        代码审查

        Args:
            code: 要审查的代码
            language: 编程语言

        Returns:
            审查结果和建议
        """
        prompt = f"""
请审查以下{language}代码：

```{language.lower()}
{code}
```

请从以下方面进行评审：
1. 代码质量和可读性
2. 潜在的bug和错误
3. 性能优化建议
4. 安全性问题
5. 最佳实践建议
"""
        return self.chat(prompt)

    def fix_bug(self, code, error_message=None, language="Python"):
        """
        修复代码bug

        Args:
            code: 有bug的代码
            error_message: 错误信息（可选）
            language: 编程语言

        Returns:
            修复后的代码和说明
        """
        error_part = f"\n错误信息：\n{error_message}\n" if error_message else ""

        prompt = f"""
以下{language}代码存在问题，请帮助修复：

```{language.lower()}
{code}
```
{error_part}
请提供：
1. 问题分析
2. 修复后的代码
3. 修改说明
"""
        return self.chat(prompt)

    def explain_code(self, code, language="Python"):
        """
        解释代码

        Args:
            code: 要解释的代码
            language: 编程语言

        Returns:
            代码解释
        """
        prompt = f"""
请详细解释以下{language}代码的功能和实现原理：

```{language.lower()}
{code}
```

请包括：
1. 整体功能说明
2. 逐行或逐块的详细解释
3. 使用的算法或设计模式
4. 时间和空间复杂度（如适用）
"""
        return self.chat(prompt)

    def optimize_code(self, code, language="Python"):
        """
        优化代码

        Args:
            code: 要优化的代码
            language: 编程语言

        Returns:
            优化后的代码和说明
        """
        prompt = f"""
请优化以下{language}代码的性能和可读性：

```{language.lower()}
{code}
```

请提供：
1. 优化分析
2. 优化后的代码
3. 优化说明和性能对比
"""
        return self.chat(prompt)


# 便捷函数
def quick_chat(prompt):
    """快速聊天函数"""
    helper = GLMHelper()
    return helper.chat(prompt)


def quick_code(description, language="Python"):
    """快速代码生成函数"""
    helper = GLMHelper()
    return helper.generate_code(description, language)


if __name__ == "__main__":
    # 简单测试
    print("GLM Helper 工具测试")
    print("=" * 50)

    try:
        helper = GLMHelper()
        print("✓ GLM Helper 初始化成功")

        # 测试代码生成
        result = helper.generate_code("实现一个计算斐波那契数列的函数")
        print("\n代码生成测试：")
        print(result)

    except Exception as e:
        print(f"错误: {e}")
