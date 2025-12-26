// 页面中使用 openid 的完整示例

Page({
  data: {
    openid: '',
    userInfo: null
  },

  onLoad() {
    // 页面加载时自动获取 openid
    this.getOpenId();
  },

  /**
   * 获取 openid
   */
  getOpenId() {
    const SERVER_URL = 'http://your-server-address:3000'; // 修改为你的服务器地址

    wx.showLoading({
      title: '获取中...',
    });

    wx.login({
      success: (res) => {
        if (res.code) {
          // 发送 code 到后端
          wx.request({
            url: `${SERVER_URL}/api/wechat/login`,
            method: 'POST',
            data: {
              code: res.code
            },
            success: (response) => {
              wx.hideLoading();

              if (response.data.success) {
                const openid = response.data.data.openid;

                // 更新页面数据
                this.setData({
                  openid: openid
                });

                // 保存到本地存储
                wx.setStorageSync('openid', openid);

                console.log('获取到 openid:', openid);

                // 可以在这里调用其他需要 openid 的接口
                this.callCozeBot(openid);
              } else {
                wx.showToast({
                  title: response.data.error || '获取失败',
                  icon: 'none'
                });
              }
            },
            fail: (err) => {
              wx.hideLoading();
              console.error('请求失败:', err);
              wx.showToast({
                title: '网络错误',
                icon: 'none'
              });
            }
          });
        }
      },
      fail: (err) => {
        wx.hideLoading();
        console.error('登录失败:', err);
      }
    });
  },

  /**
   * 调用 Coze 智能体示例
   * @param {string} openid - 用户的 openid
   */
  callCozeBot(openid) {
    // 这里是调用你的 Coze 智能体的示例
    // 你可以将 openid 作为用户标识发送给 Coze

    console.log('使用 openid 调用 Coze:', openid);

    // 示例：发送消息给 Coze
    // wx.request({
    //   url: 'https://your-coze-api-endpoint',
    //   method: 'POST',
    //   data: {
    //     user_id: openid,  // 使用 openid 作为用户标识
    //     message: '你好'
    //   }
    // });
  },

  /**
   * 按钮点击事件 - 手动获取 openid
   */
  onGetOpenIdClick() {
    this.getOpenId();
  }
});
