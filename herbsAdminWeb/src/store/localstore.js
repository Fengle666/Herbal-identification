let localStore = {
    setUserInfo(userInfo) {
        localStorage.setItem("userInfo",JSON.stringify(userInfo));
    },
    getUserInfo() {
        if(localStorage.getItem("userInfo")){
            return JSON.parse(localStorage.getItem("userInfo"))
        }else{
            return null;
        }
        
    },

}

export default localStore