window.onload =function(){
    axios({
        method: 'get',
        url: 'http://www.lijunxi.site:1234/authorization/getCaptcha',
    }).then(function (resp) {
       localStorage.setItem('hash_key', resp.data.data.hash_key);
       document.getElementById('my_captcha').innerHTML = '<img  src="http://www.lijunxi.site:1234'+resp.data.data.image_url+'" alt="">'
    });
}

document.getElementById("regiter_btn").onclick = function(){
    var username = document.getElementById('username').value
    var password1 = document.getElementById('password1').value
    var password2 = document.getElementById('password2').value
    var code = document.getElementById('code').value
    if(username == ''){
        tips.innerHTML = "用户名不能为空"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    if(username.length < 6){
        tips.innerHTML = "用户名不能少于6位"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    if(password1 == '' || password2 == ''){
        tips.innerHTML = "密码不能为空"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    if(code == ''){
        tips.innerHTML = "验证码不能为空"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    if(password1 != password2){
        tips.innerHTML = "两次输入的密码不匹配"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    axios({
        method: 'post',
        url: 'http://www.lijunxi.site:1234/authorization/register',
        data:{
            username: username,
            password: md5(password1),
            answer: code,
            hash_key: localStorage.getItem('hash_key')
        }
    }).then(function (resp) {
        if(resp.data.data == '验证不通过'){
            tips.innerHTML = "验证码错误"
            tips.setAttribute('style', 'visibility: visible')
            return
        }
        if(resp.data.data == '用户已存在'){
            tips.innerHTML = "用户已存在"
            tips.setAttribute('style', 'visibility: visible')
            return
        }
        window.location.href ="index.html";
    });


}