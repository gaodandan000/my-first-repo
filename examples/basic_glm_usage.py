#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GLM Coding 基础使用示例
Basic GLM Coding Usage Example

这个脚本展示了如何使用智谱AI的GLM模型进行代码生成和对话
This script demonstrates how to use Zhipu AI's GLM model for code generation and chat
"""

import os
from zhipuai import ZhipuAI


def init_client():
    """
    初始化GLM客户端
    Initialize GLM client
    """
    api_key = os.getenv("GLM_API_KEY")
    if not api_key:
        raise ValueError("请设置环境变量 GLM_API_KEY / Please set GLM_API_KEY environment variable")

    client = ZhipuAI(api_key=api_key)
    return client


def chat_completion(client, prompt, model="glm-4"):
    """
    基础对话完成
    Basic chat completion

    Args:
        client: ZhipuAI客户端
        prompt: 用户输入的提示词
        model: 使用的模型名称

    Returns:
        模型的响应内容
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        top_p=0.9,
    )

    return response.choices[0].message.content


def code_generation_example(client):
    """
    代码生成示例
    Code generation example
    """
    prompt = """
    请用Python写一个函数，实现快速排序算法。
    要求：
    1. 包含详细注释
    2. 包含使用示例
    3. 包含时间复杂度说明
    """

    print("=" * 50)
    print("代码生成示例 / Code Generation Example")
    print("=" * 50)
    print(f"Prompt: {prompt}\n")

    result = chat_completion(client, prompt)
    print("Response:")
    print(result)
    print("\n")


def code_review_example(client):
    """
    代码审查示例
    Code review example
    """
    code = """
def calculate(a, b):
    return a + b * 2
    """

    prompt = f"""
    请审查以下代码，并提供改进建议：

    ```python
{code}
    ```

    请从以下几个方面评审：
    1. 代码可读性
    2. 命名规范
    3. 潜在bug
    4. 性能优化
    """

    print("=" * 50)
    print("代码审查示例 / Code Review Example")
    print("=" * 50)
    print(f"Code to review:\n{code}\n")

    result = chat_completion(client, prompt)
    print("Review:")
    print(result)
    print("\n")


def bug_fixing_example(client):
    """
    Bug修复示例
    Bug fixing example
    """
    buggy_code = """
def find_max(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
    """

    prompt = f"""
    以下代码存在bug，请找出问题并提供修复后的代码：

    ```python
{buggy_code}
    ```
    """

    print("=" * 50)
    print("Bug修复示例 / Bug Fixing Example")
    print("=" * 50)
    print(f"Buggy code:\n{buggy_code}\n")

    result = chat_completion(client, prompt)
    print("Fixed code:")
    print(result)
    print("\n")


def main():
    """
    主函数
    Main function
    """
    print("GLM Coding 示例程序")
    print("GLM Coding Example Program")
    print("=" * 50)

    try:
        # 初始化客户端
        client = init_client()
        print("✓ GLM客户端初始化成功 / GLM client initialized successfully\n")

        # 运行示例
        code_generation_example(client)
        code_review_example(client)
        bug_fixing_example(client)

        print("=" * 50)
        print("所有示例运行完成！ / All examples completed!")

    except Exception as e:
        print(f"错误 / Error: {e}")


if __name__ == "__main__":
    main()
