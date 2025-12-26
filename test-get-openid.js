#!/usr/bin/env node

/**
 * 微信小程序 OpenID 获取测试工具
 * 使用方法：node test-get-openid.js <code>
 */

const https = require('https');

const APPID = 'wxd6cffbc89be42bd6';
const SECRET = 'de5c9e44a0d2235ab7ac6e7e5a72c9dc';

// 从命令行获取 code
const code = process.argv[2];

if (!code) {
  console.error('❌ 错误：请提供微信登录返回的 code');
  console.log('\n使用方法：');
  console.log('  node test-get-openid.js <你的code>');
  console.log('\n如何获取 code：');
  console.log('  在小程序中调用 wx.login() 获取 code');
  process.exit(1);
}

console.log('🔍 正在获取 OpenID...');
console.log('📱 AppID:', APPID);
console.log('🔑 Code:', code);
console.log('');

// 调用微信 API
const url = `https://api.weixin.qq.com/sns/jscode2session?appid=${APPID}&secret=${SECRET}&js_code=${code}&grant_type=authorization_code`;

https.get(url, (res) => {
  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('end', () => {
    try {
      const result = JSON.parse(data);

      if (result.errcode) {
        console.error('❌ 获取失败：');
        console.error('   错误码:', result.errcode);
        console.error('   错误信息:', result.errmsg);
        console.log('\n常见错误：');
        console.log('   40029: code 无效或已使用（code 只能使用一次）');
        console.log('   40163: code 已过期（code 有效期5分钟）');
      } else {
        console.log('✅ 获取成功！');
        console.log('');
        console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
        console.log('📋 结果信息：');
        console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
        console.log('OpenID:     ', result.openid);
        console.log('Session Key:', result.session_key);
        if (result.unionid) {
          console.log('UnionID:    ', result.unionid);
        }
        console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
      }
    } catch (error) {
      console.error('❌ 解析响应失败:', error.message);
      console.log('原始响应:', data);
    }
  });

}).on('error', (error) => {
  console.error('❌ 请求失败:', error.message);
});
