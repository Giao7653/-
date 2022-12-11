var idx = 2;
var is = true;
function scrollBottomOrTop() {
    var clients = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
    var scrollTop = document.documentElement.scrollTop;
    // 这里存在兼容问题，会把body当成div来处理，如果用document.body.scrollHeight就得不到正确的高度，用body时需要把doctype后面的html去掉
    // 这里没用body，而是用到documentElement
    var wholeHeight = document.documentElement.scrollHeight;
    if (clients + scrollTop >= wholeHeight && is == true) {
        axios({
            method: 'get',
            url: 'http://www.lijunxi.site:1234/page/getStemInTime',
            params:{page_num:idx}
        }).then(function (resp) {
            if(resp.data.data == '页数超出范围'){
                document.getElementById('geng').innerHTML += "<div class='geng-low'></div>";
                is = false;
                return;
            }
            for(i = 0; i < 500000000; i++){}
        
            var str = "";
            for (i = 0; i < resp.data.data.length; i++) { 
                if(resp.data.data[i].stem_image[0] == undefined){
                var t = resp.data.data[i].content
                var strContent = ""
                var number = 0
                var is_ture = 0
                for(j = 0; j < t.length; j++){
                    if(is_ture == 1 && t[j] == '<' && t[j+1] == 'p')  break; 
                    if(t.charCodeAt(j) > 255 && number < 250) strContent += t[j], number ++;
                    else if(t.charCodeAt(j) > 255 && number == 250 && is_ture == 0) strContent += "......", is_ture = 1;
                    else if(t.charCodeAt(j) <= 255) strContent += t[j];
                }
                strContent += '<div style="text-align:right;"><a href="stemhome.html?stem_id='+resp.data.data[i].stem_id+'" style="color: #bc894b;font-size:14px">点击查看更多</a></div>'
                str += '<div class="geng-part" id="geng-part'+(i+1)+'"><span class="topic"><a href="stemhome.html?stem_id='+resp.data.data[i].stem_id+'">'+resp.data.data[i].stem+'</a></span><div class="introduce"><a href="stemhome.html?stem_id='+resp.data.data[i].stem_id+'">'+strContent+'</a></div></div>' 
            } 
            else{
                var t = resp.data.data[i].content
                var strContent = ""
                var number = 0
                var is_ture = 0
                for(j = 0; j < t.length; j++){
                    if(is_ture == 1 && t[j] == '<' && t[j+1] == 'p')  break; 
                    if(t.charCodeAt(j) > 255 && number < 90) strContent += t[j], number ++;
                    else if(t.charCodeAt(j) > 255 && number == 90 && is_ture == 0) strContent += "......", is_ture = 1;
                    else if(t.charCodeAt(j) <= 255) strContent += t[j];
                }
                if(number == 90) strContent += '<div style="text-align:right;"><a href="stemhome.html?stem_id='+resp.data.data[i].stem_id+'" style="color: #bc894b;font-size:14px">点击查看更多</a></div>'
                str += "<div class='geng-part' id='geng-part"+(i+1)+"'><span class='topic'><a href='stemhome.html?stem_id="+resp.data.data[i].stem_id+"'>"+resp.data.data[i].stem+"</a></span><div class='introduce'><a href='stemhome.html?stem_id="+resp.data.data[i].stem_id+"'>"+strContent+"</a></div><div class='linkof'><a><img src='http://www.lijunxi.site:1234/"+resp.data.data[i].stem_image[0]+"'></a></div></div>"
            }
            }
            document.getElementById('geng').innerHTML += str;
            idx++;

        });



        // 在实际应用中可以通过请求后台获取下一页的数据，然后显示到当前位置，就能达到按页加载的效果。

    }
}

function scrollBottomOrTop2() {
    var scrollTop = document.documentElement.scrollTop;
    // 这里存在兼容问题，会把body当成div来处理，如果用document.body.scrollHeight就得不到正确的高度，用body时需要把doctype后面的html去掉
    // 这里没用body，而是用到documentElement
    // console.log(scrollTop)
       if (390 <= scrollTop) {
        document.getElementById('head').setAttribute("style", "background-color:rgb(249, 232, 232);transition: all 0.6s ease 0s;opacity: 0.9;")
    }
    else{
        document.getElementById('head').setAttribute("style", "background-color:rgb(48, 81, 100);transition: all 0.6s ease 0s;")
    }
}

// 一个页面绑定多个滚动事件
function addEvent(obj,type,fn){
    if(obj.attachEvent){ //ie
        obj.attachEvent('on'+type,function(){
            fn.call(obj);
        })
    }else{
        obj.addEventListener(type,fn,false);
    }
}
addEvent(window,'scroll',function(){
    scrollBottomOrTop();
});
addEvent(window,'scroll',function(){
    scrollBottomOrTop2();
});