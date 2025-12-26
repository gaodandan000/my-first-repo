#!/usr/bin/env node
/**
 * 测试智谱AI API连接 (Node.js)
 */

// 检查环境变量
const apiKey = process.env.ANTHROPIC_API_KEY;
const apiBase = process.env.ANTHROPIC_API_BASE;

if (!apiKey) {
    console.log('❌ 错误：未找到 ANTHROPIC_API_KEY 环境变量');
    console.log('请先运行: source .env 或使用 glm 命令');
    process.exit(1);
}

console.log(`🔑 API Key: ${apiKey.substring(0, 20)}...`);
console.log(`🌐 API Base: ${apiBase}`);
console.log('\n✅ 环境变量加载成功！');
console.log('\n📝 注意：实际 API 调用需要安装 @anthropic-ai/sdk：');
console.log('   npm install @anthropic-ai/sdk');
console.log('\n示例代码：');
console.log(`
const Anthropic = require('@anthropic-ai/sdk');

const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
    baseURL: process.env.ANTHROPIC_API_BASE
});

// 使用 client 进行 API 调用
`);
