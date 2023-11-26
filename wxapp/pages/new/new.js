const app = getApp()
Page({
  data: {
    defaultImage: false,                   //初始不加载图片，等后续拍照后显示图片
    cameraHidden: true,                       //初始camera打开摄像头功能关闭
    takeHidden: true,                        //初始可以有拍照功能
    tempfilepathimg: null,             //加载本地图片初始值为null
    take_image: '',                         //设置识别返回的图片结果初始值
    src: '',
    food: '等待中',
    time: ''
  },

  onLoad: function (options) {
    self=this//没有这步编译不通过，self可以改成其他变量名
  },

  //点击打开相机后执行以下命令
  open() {
    this.setData({
      defaultImage: true,           //初始的页面可以被替换
      cameraHidden: false,          //可以使用carame功能，打开摄像头
      tempfilepathimg: '',    //当打开相机时 以下内容都是在初始值
      take_image: ''
    })
  },


  takePhoto: function() {
    let that = this;
    const ctx = wx.createCameraContext()
    ctx.takePhoto({
      quality: 'high',
      success: (res) => {
        that.setData({                   //接口调用成功的回调函数
          cameraHidden: true,         //当拍照功能执行时，相机功能关闭
          takeHidden: false,          //隐藏该内容
          take_image: res.tempImagePath,              //相机拍摄的照片赋给take_image中
          tempfilepathimg: res.tempImagePath             //替换
        })
      }
    })
  },


  click() {
    let that = this;
    const filepath = this.data.tempfilepathimg;     //获得上一步的加载本地图像的图像
        wx.uploadFile({
          url:"http://127.0.0.1:4399/",             //接口地址 
          filePath: filepath,                           //需要处理的图片
          name: 'file',    
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

  initCamera() {
    this.setData({
      defaultImage: true,
      cameraHidden: false,
      takeHidden: false
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



