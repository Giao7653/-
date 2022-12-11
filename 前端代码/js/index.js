window.onload =function() {
    axios({
        method: 'get',
        url: 'http://www.lijunxi.site:1234/stem/todayRecommend',
    }).then(function (resp) {
        var s = '';
        for(i = 0; i < resp.data.data.length; i++){
            s += '<li><span>' + (i+1) + '</span><a href="stemhome.html?stem_id=' + resp.data.data[i].stem_id + '">' + resp.data.data[i].stem + '</a></li>'
        }
        document.getElementById('recommand').innerHTML = s;
    });

    axios({
        method: 'get',
        url: 'http://www.lijunxi.site:1234/stem/getStemInTime',
    }).then(function (resp) {
        var str = "";
        for (i = 0; i < resp.data.data.length; i++) { 
            if(resp.data.data[i].stem_image[0] == undefined){
                var t = resp.data.data[i].content
                var strContent = ""
                var number = 0
                var is = 0
                for(j = 0; j < t.length; j++){
                    if(is == 1 && t[j] == '<' && t[j+1] == 'p')  break; 
                    if(t.charCodeAt(j) > 255 && number < 250) strContent += t[j], number ++;
                    else if(t.charCodeAt(j) > 255 && number == 250 && is == 0) strContent += "......", is = 1;
                    else if(t.charCodeAt(j) <= 255) strContent += t[j];
                }
                strContent += '<div style="text-align:right;"><a href="stemhome.html?stem_id='+resp.data.data[i].stem_id+'" style="color: #bc894b;font-size:14px">点击查看更多</a></div>'
                str += '<div class="geng-part" id="geng-part'+(i+1)+'"><span class="topic"><a href="stemhome.html?stem_id='+resp.data.data[i].stem_id+'">'+resp.data.data[i].stem+'</a></span><div class="introduce"><a href="stemhome.html?stem_id='+resp.data.data[i].stem_id+'">'+strContent+'</a></div></div>' 
            } 
            else{
                var t = resp.data.data[i].content
                var strContent = ""
                var number = 0
                var is = 0
                for(j = 0; j < t.length; j++){
                    if(is == 1 && t[j] == '<' && t[j+1] == 'p')  break; 
                    if(t.charCodeAt(j) > 255 && number < 90) strContent += t[j], number ++;
                    else if(t.charCodeAt(j) > 255 && number == 90 && is == 0) strContent += "......", is = 1;
                    else if(t.charCodeAt(j) <= 255) strContent += t[j];
                }
                if(number == 90) strContent += '<div style="text-align:right;"><a href="stemhome.html?stem_id='+resp.data.data[i].stem_id+'" style="color: #bc894b;font-size:14px">点击查看更多</a></div>'
                str += "<div class='geng-part' id='geng-part"+(i+1)+"'><span class='topic'><a href='stemhome.html?stem_id="+resp.data.data[i].stem_id+"'>"+resp.data.data[i].stem+"</a></span><div class='introduce'><a href='stemhome.html?stem_id="+resp.data.data[i].stem_id+"'>"+strContent+"</a></div><div class='linkof'><a><img src='http://www.lijunxi.site:1234/"+resp.data.data[i].stem_image[0]+"'></a></div></div>"
            }
        }
        // str += '<div class="index_add"><button>点击加载更多内容</button></div>'
        document.getElementById('geng').innerHTML = str;
    });

    axios({
        method: 'get',
        url: 'http://www.lijunxi.site:1234/stem/searchTimesHot',
    }).then(function (resp) {
        var str = "";
        for (i = 0; i < resp.data.data.length; i++) { 
            str += '<li><a href="search.html?stem='+resp.data.data[i]['search_content']+'">'+resp.data.data[i]['search_content']+'</a></li>'
        }
        document.getElementById('my_hot_search').innerHTML = str;
    });

    var my_login = document.getElementById('login_box')
    var my_token = localStorage.getItem('token');
    if(my_token != null){
        var username = localStorage.getItem('username');
        if(username == null){
            my_login.innerHTML = ```a href = "javascript:void(0)" onclick = "document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block';">登录</a>```
            return;
        }
        axios({
            method: 'get',
            url: 'http://www.lijunxi.site:1234/userhome/getUserInfo',
            params:{
                username:username,
                token:my_token
            }
        }).then(function (resp) {
            if(resp.data.data == '身份验证失败，请重新登录'){
                my_login.innerHTML = `<a href = "javascript:void(0)" onclick = "document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block';">登录</a>`
                return;
            }
            var str = '<div class="dropdown"><div class="image"><img src="http://www.lijunxi.site:1234/'+resp.data.data['avatar']+'" width="50px"></div><div class="dropdown-content"><a href="userhome.html?username='+username+'"><svg t="1665553673557" class="icon" viewBox="100 0 1024 690" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2918" width="25px" height="25px"><path d="M224 800h-64a256.032 256.032 0 0 1 149.28-232.768 160 160 0 1 1 213.408 0A256.032 256.032 0 0 1 672 800h-64a192 192 0 1 0-384 0z m608 96h64.288A64.128 64.128 0 0 0 960 831.84V192.16A63.936 63.936 0 0 0 896.288 128H127.68A64.128 64.128 0 0 0 64 192.16v639.68C64 867.296 92.544 896 127.712 896H128V223.744A31.872 31.872 0 0 1 160 192h704c17.664 0 32 14.56 32 31.744v576.512A31.872 31.872 0 0 1 864 832h-32v64zM415.936 544a96 96 0 1 0 0-192 96 96 0 0 0 0 192zM640 480c0-17.664 14.016-32 32.096-32h159.808A31.968 31.968 0 0 1 864 480c0 17.664-14.016 32-32.096 32H672.096A31.968 31.968 0 0 1 640 480zM128 832h704v64H128v-64z m512-224c0-17.664 14.208-32 32-32h96c17.664 0 32 14.208 32 32 0 17.664-14.208 32-32 32h-96c-17.664 0-32-14.208-32-32z" p-id="2919"></path></svg>个人中心</a><a onclick="loginout();"><svg t="665554457378" class="icon" viewBox="50 0 1024 890" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3822" width="25px" height="25px"><path d="M960.512 539.712l-144.768 144.832-48.256-48.256 60.224-60.288H512V512h325.76l-70.272-70.272 48.256-48.256 144.768 144.768-0.704 0.768 0.704 0.704zM704 192a64 64 0 0 0-64-64H192a64 64 0 0 0-64 64v640a64 64 0 0 0 64 64h448a64 64 0 0 0 64-64v-64h64v64a128 128 0 0 1-128 128H192a128 128 0 0 1-128-128V192a128 128 0 0 1 128-128h448a128 128 0 0 1 128 128v128h-64V192z" p-id="3823"></path></svg>退出登录</a></div></div>'
            my_login.innerHTML = str
            return;
        });  
    }
    else{
        my_login.innerHTML = `<a href = "javascript:void(0)" onclick = "document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block';">登录</a>`
    }
    


    var input = document.getElementsByTagName("input")[0]
    var box = document.getElementsByClassName("search_box")[0]
    var input_box = document.getElementById("searchStem")
    input.onclick=function(event){
        box.style.display="block"
        input_box.setAttribute('style', 'border-radius:10px 10px 0 0')
        event.stopPropagation()//这里是关键，阻止冒泡
    }
    document.onclick=function(){
        box.style.display="none"//点击文档document隐藏box
        input_box.setAttribute('style', 'border-radius: 24px')
    }
    box.onclick=function(event){
        event.stopPropagation()//点击box本身，阻止冒泡
    }

    // 存储本地搜索
    local_search = "";
    get_search_data = JSON.parse(localStorage.getItem('search_data'))
    if(get_search_data != null){
        for(i = get_search_data.length - 1; i >= get_search_data.length - 8 && i >= 0; i --){
            local_search += "<li><a href='search.html?stem="+get_search_data[i]+"'>"+get_search_data[i]+"</a></li>"
        }
    }
 
    document.getElementById('my_loacl_search').innerHTML = local_search 
};


//   document.getElementById("a").onclick = function(){
//       axios.withCredentials = true;
//     axios.defaults.withCredentials = true;
//     axios({
//       method: 'get',
//       url: 'http://127.0.0.1:8000/stem/test',
//     });
// }