const express = require('express');
const axios = require('axios');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// 微信小程序配置
const WECHAT_CONFIG = {
  appId: process.env.WECHAT_APPID || 'wxd6cffbc89be42bd6',
  appSecret: process.env.WECHAT_APPSECRET || 'de5c9e44a0d2235ab7ac6e7e5a72c9dc'
};

// 中间件
app.use(cors());
app.use(express.json());

// 健康检查接口
app.get('/', (req, res) => {
  res.json({
    status: 'ok',
    message: '微信小程序 OpenID 获取服务运行中',
    timestamp: new Date().toISOString()
  });
});

// 获取 openid 接口
app.post('/api/wechat/login', async (req, res) => {
  try {
    const { code } = req.body;

    // 验证参数
    if (!code) {
      return res.status(400).json({
        success: false,
        error: '缺少 code 参数'
      });
    }

    // 调用微信 API 获取 openid
    const url = 'https://api.weixin.qq.com/sns/jscode2session';
    const response = await axios.get(url, {
      params: {
        appid: WECHAT_CONFIG.appId,
        secret: WECHAT_CONFIG.appSecret,
        js_code: code,
        grant_type: 'authorization_code'
      }
    });

    const data = response.data;

    // 检查是否有错误
    if (data.errcode) {
      return res.status(400).json({
        success: false,
        error: data.errmsg,
        errcode: data.errcode
      });
    }

    // 返回成功结果
    res.json({
      success: true,
      data: {
        openid: data.openid,
        session_key: data.session_key,
        unionid: data.unionid || null
      }
    });

  } catch (error) {
    console.error('获取 openid 失败:', error.message);
    res.status(500).json({
      success: false,
      error: '服务器内部错误',
      message: error.message
    });
  }
});

// 启动服务器
app.listen(PORT, () => {
  console.log(`服务器运行在 http://localhost:${PORT}`);
  console.log(`微信 AppID: ${WECHAT_CONFIG.appId}`);
  console.log('API 端点: POST /api/wechat/login');
});
