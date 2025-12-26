# my-first-repo

用来存我的AI项目/脚本/文档

## GLM Coding 项目

这是一个基于智谱AI GLM模型的代码辅助工具项目，提供代码生成、审查、优化等功能。

This is a coding assistant project based on Zhipu AI's GLM model, providing code generation, review, optimization and more.

## 项目结构 / Project Structure

```
my-first-repo/
├── config/              # 配置文件 / Configuration files
│   └── glm_config.yaml  # GLM配置 / GLM configuration
├── src/                 # 源代码 / Source code
│   ├── __init__.py
│   └── glm_helper.py    # GLM助手工具类 / GLM helper utilities
├── examples/            # 示例代码 / Example code
│   └── basic_glm_usage.py
├── scripts/             # 脚本 / Scripts
│   └── setup.sh         # 环境设置脚本 / Setup script
├── docs/                # 文档 / Documentation
├── tests/               # 测试 / Tests
├── logs/                # 日志 / Logs
├── models/              # 模型文件 / Model files
├── .env.example         # 环境变量模板 / Environment template
├── .gitignore
├── requirements.txt     # Python依赖 / Python dependencies
└── README.md
```

## 快速开始 / Quick Start

### 1. 环境要求 / Requirements

- Python 3.8+
- 智谱AI API Key (从 https://open.bigmodel.cn/ 获取)

### 2. 安装 / Installation

#### 自动安装 / Automatic Setup

```bash
# 运行设置脚本
./scripts/setup.sh
```

#### 手动安装 / Manual Setup

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/Mac
# 或 Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 复制环境变量模板
cp .env.example .env
```

### 3. 配置 / Configuration

编辑 `.env` 文件，设置你的 API Key：

```bash
GLM_API_KEY=your_api_key_here
```

### 4. 运行示例 / Run Examples

```bash
# 运行基础示例
python examples/basic_glm_usage.py

# 使用GLM Helper
python -c "from src.glm_helper import quick_chat; print(quick_chat('你好'))"
```

## 功能特性 / Features

### 1. 代码生成 / Code Generation
- 根据描述生成代码
- 支持多种编程语言
- 自动添加注释和文档

### 2. 代码审查 / Code Review
- 检查代码质量
- 发现潜在bug
- 提供优化建议

### 3. Bug修复 / Bug Fixing
- 自动识别代码问题
- 提供修复方案
- 解释修改原因

### 4. 代码优化 / Code Optimization
- 性能优化建议
- 代码重构建议
- 最佳实践应用

### 5. 代码解释 / Code Explanation
- 详细解释代码逻辑
- 分析算法复杂度
- 识别设计模式

## 使用示例 / Usage Examples

### Python API 使用

```python
from src.glm_helper import GLMHelper

# 初始化助手
helper = GLMHelper()

# 生成代码
code = helper.generate_code("实现一个二分查找算法", language="Python")
print(code)

# 审查代码
review = helper.review_code("""
def add(a, b):
    return a + b
""")
print(review)

# 修复bug
fixed = helper.fix_bug("""
def divide(a, b):
    return a / b
""", error_message="ZeroDivisionError")
print(fixed)
```

### 快捷函数使用

```python
from src.glm_helper import quick_chat, quick_code

# 快速对话
response = quick_chat("解释一下什么是递归")
print(response)

# 快速生成代码
code = quick_code("实现冒泡排序", language="Python")
print(code)
```

## 配置说明 / Configuration

配置文件位于 `config/glm_config.yaml`，可以自定义：

- API设置（超时、URL等）
- 模型参数（temperature、top_p、max_tokens）
- 代码生成偏好
- 日志设置

## 开发指南 / Development Guide

### 添加新功能

1. 在 `src/` 目录下创建新模块
2. 在 `examples/` 添加使用示例
3. 更新 `requirements.txt` 如有新依赖
4. 运行测试确保功能正常

### 运行测试

```bash
# 安装测试依赖
pip install pytest

# 运行测试
pytest tests/
```

### 代码规范

使用 black 和 flake8 保持代码质量：

```bash
# 格式化代码
black src/ examples/

# 检查代码质量
flake8 src/ examples/
```

## 常见问题 / FAQ

### Q: 如何获取 GLM API Key?
A: 访问 https://open.bigmodel.cn/ 注册账号并创建 API Key

### Q: 支持哪些模型?
A: 支持 glm-4, glm-4-plus, glm-4-air, glm-4-flash, glm-3-turbo 等

### Q: 如何处理 API 调用限制?
A: 在配置文件中调整超时设置，或升级 API 套餐

### Q: 可以离线使用吗?
A: 本工具需要联网调用智谱AI API，暂不支持离线使用

## 贡献 / Contributing

欢迎提交 Issue 和 Pull Request！

## 许可证 / License

MIT License

## 资源链接 / Resources

- 智谱AI开放平台: https://open.bigmodel.cn/
- GLM API文档: https://open.bigmodel.cn/dev/api
- Python SDK: https://github.com/zhipuai/zhipuai-sdk-python

## 更新日志 / Changelog

### v0.1.0 (2025-12-26)
- ✨ 初始化项目结构
- ✨ 添加 GLM Helper 工具类
- ✨ 添加基础示例代码
- ✨ 添加配置管理
- 📝 完善项目文档
