# 微信小程序 OpenID 获取完整指南

## 项目简介

这是一个完整的微信小程序 OpenID 获取解决方案，包含：
- Node.js 后端服务（Express）
- 微信小程序前端示例代码
- 完整的配置和部署说明

## 目录结构

```
my-first-repo/
├── server/                    # 后端服务
│   ├── index.js              # 主服务文件
│   ├── package.json          # 依赖配置
│   ├── .env                  # 环境变量（已配置）
│   ├── .env.example          # 环境变量模板
│   └── .gitignore           # Git 忽略配置
└── miniprogram-example/      # 小程序示例代码
    ├── login.js              # 登录工具函数
    ├── page-example.js       # 页面 JS 示例
    ├── page-example.wxml     # 页面 WXML 示例
    └── page-example.wxss     # 页面样式示例
```

## 快速开始

### 第一步：安装后端服务

```bash
# 进入服务器目录
cd server

# 安装依赖
npm install

# 启动服务
npm start
```

服务将在 http://localhost:3000 启动。

### 第二步：配置环境变量

环境变量已在 `server/.env` 文件中配置：

```env
WECHAT_APPID=wxd6cffbc89be42bd6
WECHAT_APPSECRET=de5c9e44a0d2235ab7ac6e7e5a72c9dc
PORT=3000
```

### 第三步：部署到服务器

你需要将后端服务部署到一个公网可访问的服务器上。推荐方式：

#### 方式 1：腾讯云服务器
1. 购买一台云服务器
2. 安装 Node.js
3. 上传代码到服务器
4. 运行 `npm install && npm start`

#### 方式 2：使用云函数（推荐）
- 腾讯云云函数
- 阿里云函数计算
- AWS Lambda

#### 方式 3：使用 Vercel/Railway 等平台
免费且简单，适合测试使用。

### 第四步：配置小程序

1. 将 `miniprogram-example` 中的代码复制到你的小程序项目
2. 修改 `SERVER_URL` 为你的服务器地址

```javascript
const SERVER_URL = 'https://your-domain.com'; // 改为你的服务器地址
```

3. 在微信小程序后台配置服务器域名：
   - 登录 [微信公众平台](https://mp.weixin.qq.com)
   - 开发 → 开发管理 → 开发设置 → 服务器域名
   - 添加你的服务器域名到 request 合法域名

## API 接口文档

### 1. 健康检查

**接口：** `GET /`

**响应示例：**
```json
{
  "status": "ok",
  "message": "微信小程序 OpenID 获取服务运行中",
  "timestamp": "2024-01-01T00:00:00.000Z"
}
```

### 2. 获取 OpenID

**接口：** `POST /api/wechat/login`

**请求参数：**
```json
{
  "code": "微信登录返回的 code"
}
```

**成功响应：**
```json
{
  "success": true,
  "data": {
    "openid": "用户的 openid",
    "session_key": "会话密钥",
    "unionid": "unionid（如果有）"
  }
}
```

**失败响应：**
```json
{
  "success": false,
  "error": "错误信息"
}
```

## 小程序使用示例

### 基础用法

```javascript
// 引入登录函数
const { getWechatOpenId } = require('./login.js');

// 获取 openid
getWechatOpenId()
  .then(result => {
    console.log('OpenID:', result.openid);
    // 使用 openid 进行后续操作
  })
  .catch(error => {
    console.error('获取失败:', error);
  });
```

### 在 Coze 智能体中使用

```javascript
// 获取 openid 后，发送给 Coze
getWechatOpenId()
  .then(result => {
    // 调用 Coze API，将 openid 作为用户标识
    wx.request({
      url: 'https://your-coze-api.com/chat',
      method: 'POST',
      data: {
        user_id: result.openid,  // 使用 openid 标识用户
        message: '你好，智能体'
      },
      success: (res) => {
        console.log('Coze 响应:', res.data);
      }
    });
  });
```

## 常见问题

### Q1: 获取 openid 失败，提示 "invalid code"
**原因：** code 只能使用一次，且有效期为 5 分钟。
**解决：** 确保每次调用都使用新的 code。

### Q2: 小程序请求失败，提示 "不在以下 request 合法域名列表中"
**原因：** 未在微信公众平台配置服务器域名。
**解决：** 在微信公众平台添加服务器域名到白名单。

### Q3: 本地测试时如何调试？
**解决：**
1. 在微信开发者工具中勾选"不校验合法域名"
2. 使用 `http://localhost:3000` 进行本地测试

### Q4: 如何保护 AppSecret 安全？
**建议：**
1. 使用环境变量存储（已实现）
2. 不要将 `.env` 文件提交到 Git（已配置 .gitignore）
3. 生产环境使用更安全的密钥管理服务

## 生产环境部署建议

### 安全性
- [ ] 使用 HTTPS 协议
- [ ] 不要将 AppSecret 硬编码
- [ ] 定期更换 AppSecret
- [ ] 添加请求频率限制
- [ ] 添加日志记录

### 稳定性
- [ ] 使用 PM2 等进程管理器
- [ ] 配置错误监控
- [ ] 添加健康检查
- [ ] 配置负载均衡

### 示例：使用 PM2 部署

```bash
# 安装 PM2
npm install -g pm2

# 启动服务
pm2 start index.js --name wechat-openid-server

# 查看状态
pm2 status

# 查看日志
pm2 logs

# 设置开机自启
pm2 startup
pm2 save
```

## 技术支持

如有问题，请参考：
- [微信小程序官方文档](https://developers.weixin.qq.com/miniprogram/dev/api/)
- [wx.login API](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html)
- [code2Session 接口](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/user-login/code2Session.html)

## 配置信息

- **微信 AppID**: wxd6cffbc89be42bd6
- **服务端口**: 3000
- **API 端点**: POST /api/wechat/login

## 下一步

1. ✅ 后端服务已配置完成
2. ⏭️ 将后端服务部署到公网服务器
3. ⏭️ 在小程序中集成示例代码
4. ⏭️ 配置微信公众平台服务器域名
5. ⏭️ 在 Coze 智能体中使用 openid

祝你使用愉快！
