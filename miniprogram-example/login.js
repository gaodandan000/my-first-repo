// 小程序登录获取 openid 示例代码
// 将此代码添加到你的小程序页面或 app.js 中

// 配置你的后端服务器地址
const SERVER_URL = 'http://your-server-address:3000'; // 修改为你的服务器地址

/**
 * 获取微信小程序 openid
 * @returns {Promise} 返回包含 openid 的 Promise
 */
function getWechatOpenId() {
  return new Promise((resolve, reject) => {
    // 第一步：调用 wx.login 获取 code
    wx.login({
      success: (loginRes) => {
        if (loginRes.code) {
          console.log('获取到 code:', loginRes.code);

          // 第二步：将 code 发送到后端服务器
          wx.request({
            url: `${SERVER_URL}/api/wechat/login`,
            method: 'POST',
            data: {
              code: loginRes.code
            },
            header: {
              'content-type': 'application/json'
            },
            success: (res) => {
              console.log('服务器响应:', res.data);

              if (res.data.success) {
                // 成功获取 openid
                const { openid, session_key, unionid } = res.data.data;
                console.log('获取到 openid:', openid);

                // 可以将 openid 存储到本地
                wx.setStorageSync('openid', openid);

                resolve({
                  openid,
                  session_key,
                  unionid
                });
              } else {
                reject(new Error(res.data.error || '获取 openid 失败'));
              }
            },
            fail: (err) => {
              console.error('请求失败:', err);
              reject(err);
            }
          });
        } else {
          console.error('登录失败:', loginRes.errMsg);
          reject(new Error(loginRes.errMsg));
        }
      },
      fail: (err) => {
        console.error('wx.login 调用失败:', err);
        reject(err);
      }
    });
  });
}

/**
 * 使用示例
 */
function loginExample() {
  // 显示加载提示
  wx.showLoading({
    title: '登录中...',
  });

  getWechatOpenId()
    .then((result) => {
      wx.hideLoading();
      console.log('登录成功，openid:', result.openid);

      // 这里可以继续你的业务逻辑
      // 比如将 openid 发送给你的 Coze 智能体

      wx.showToast({
        title: '登录成功',
        icon: 'success'
      });
    })
    .catch((error) => {
      wx.hideLoading();
      console.error('登录失败:', error);

      wx.showToast({
        title: '登录失败',
        icon: 'none'
      });
    });
}

// 导出函数供其他页面使用
module.exports = {
  getWechatOpenId,
  loginExample
};
