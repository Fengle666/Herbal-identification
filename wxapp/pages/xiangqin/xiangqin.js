//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: 'Hello World',
    list: {},
    hasUserInfo: false,
  },
  //事件处理函数
  onLoad: function (e) {
    let that = this;
    wx.request({
    url: 'http://127.0.0.1:8000/wikipedia/wikipedia/',
    data: {name:e.name},
    method: 'GET', 
    success: function(res){
      // success
      console.log(res.data.results[0])
      that.setData({
        list:res.data.results[0]
      })
    },
    fail: function() {
      // fail
    },
    complete: function() {
      // complete
    }
    })
  },

})
