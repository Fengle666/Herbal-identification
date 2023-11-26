// index.js
// 获取应用实例
const app = getApp()

Page({
  data: {
    tempfilepathimg: null,             //加载本地图片初始值为null
    src: '',
    food: '等待中',
    time: ''
  },

  onLoad: function (options) {
    self=this//没有这步编译不通过，self可以改成其他变量名
  },

  send:function()
  {
    let that = this;
   wx.chooseImage({
     count: 1,
     sizeType: ['original', 'compressed'],
     sourceType: ['album'],
     success (res) {
       // tempFilePath可以作为img标签的src属性显示图片
       that.setData({tempfilepathimg: res.tempFilePaths[0]})//tempFilePaths为一个数组，显示数组第一个元素
     }
   })
  },

  xiangqin:function(){
    wx.navigateTo({
      url: '../xiangqin/xiangqin?name='+this.data.food
    })
  },

  click() {
    let that = this;
    const filepath = this.data.tempfilepathimg;     //获得上一步的加载本地图像的图像
        wx.uploadFile({
          url:"http://127.0.0.1:4399/",  
          filePath: filepath,                           //需要处理的图片
          name: 'file',                            //接口对应的文件名
          formData: {
            'user': 'test'
          },                        //接口对应的文件名
          success(res) {
            console.log(res)
            var str = res.data
            if (str.length > 2 && str.length < 1000) {
              that.setData({
                src: res.data,
                food: str.trim().split(" ")[0],
                time: str.trim().split(" ")[1]
              })
              console.log(str.trim().split(" ")[0])
            }
          }
        })
  },


  clear() {            //点击清除按钮后，变回初始值
    this.setData({           
      src: '',
      food: '等待中',
      time: '',
      tempfilepathimg: '',
      cameraHidden: false,
      takeHidden: true,
      take_image: ''
    })
  },


  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  }
})