document.getElementById("login").onclick = function(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value; 
    var tips = document.getElementById("tips");
    if(username == ""){
        tips.innerHTML = "请输入你的账号"
        tips.setAttribute('style', 'visibility: visible')
        return;
    }
    else if(password == ""){
        tips.innerHTML = "请输入你的密码"
        tips.setAttribute('style', 'visibility: visible')
        return;
    }

    axios({
        method: 'post',
        url: 'http://www.lijunxi.site:1234/authorization/login',
        data:{
            username: username,
            password: md5(password)
        }
    }).then(function (resp) {
        if(resp.data.data == '用户不存在'){
            tips.innerHTML = "用户不存在"
            tips.setAttribute('style', 'visibility: visible')
            return;
        }
        else if(resp.data.data == '账号或者密码错误'){
            tips.innerHTML = "账号或者密码错误"
            tips.setAttribute('style', 'visibility: visible')
            return;
        }
        else if(resp.data.data == '请求方法错误'){
            tips.innerHTML = "请求方法错误，请联系管理员"
            tips.setAttribute('style', 'visibility: visible')
            return;
        }
        localStorage.setItem('token', resp.data['token'])
        localStorage.setItem('username', resp.data['username'])
        location.reload();
    });

}

// document.getElementById("loginout").onclick = function(){
//     // var username = localStorage.getItem('username');
//     // var my_token = localStorage.getItem('token');
//     // if(username != null) localStorage.removeItem('username');
//     // if(my_token != null) localStorage.removeItem('token');
//     axios({
//         method: 'get',
//         url: 'http://127.0.0.1:8000/authorization/login_out',
//     }).then(function (resp) {
//        console.log(resp.data)
//     });
//     location.reload();
// }
function loginout(){
    // axios.withCredentials = true;
    // axios.defaults.withCredentials = true;
    // axios({
    //     method: 'get',
    //     url: 'http://127.0.0.1:8000/authorization/login_out',
    // }).then(function (resp) {
    //    console.log(resp.data)
    // });
    var username = localStorage.getItem('username');
    var my_token = localStorage.getItem('token');
    if(username != null) localStorage.removeItem('username');
    if(my_token != null) localStorage.removeItem('token');
    window.location.href = "index.html"
}


