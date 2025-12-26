#!/usr/bin/env python3
"""
测试智谱AI API连接
"""
import os
from zhipuai import ZhipuAI

# 从环境变量读取API密钥
api_key = os.environ.get("ANTHROPIC_API_KEY")
api_base = os.environ.get("ANTHROPIC_API_BASE")

if not api_key:
    print("❌ 错误：未找到 ANTHROPIC_API_KEY 环境变量")
    print("请先运行: source .env")
    exit(1)

print(f"🔑 API Key: {api_key[:20]}...")
print(f"🌐 API Base: {api_base}")
print("\n正在测试连接...")

try:
    client = ZhipuAI(api_key=api_key)

    # 测试一个简单的调用
    response = client.chat.completions.create(
        model="glm-4-flash",  # 使用快速模型进行测试
        messages=[
            {"role": "user", "content": "你好，请用一句话介绍你自己"}
        ],
        max_tokens=100
    )

    print("✅ 连接成功！")
    print(f"\n回复: {response.choices[0].message.content}")

except Exception as e:
    print(f"❌ 连接失败: {str(e)}")
    exit(1)
