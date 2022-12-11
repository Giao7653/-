var img = []; //创建一个空对象用来保存传入的图片
$(function() {
	var AllowImgFileSize = '101376'; //1兆
	$("#inputs").change(function() {
	var fil = this.files;
	for(var i = 0; i < fil.length; i++) {
	var curr = $('#inputs')[i].files[0].size;
	if(curr > AllowImgFileSize * 101376) { //当图片大于1兆提示
	layer.msg("图片文件大小超过限制 请上传小于99M的文件");
	} else {
	reads(fil[i]);
	img.push($('#inputs')[i].files[0]); //将传入的图片push到空对象中
	}
	}
	if(img.length >= 6) { //判断图片的数量，数量不能超过3张
	$('.uploadDIv').hide();
	} else {
	$('.uploadDIv').show();
	}
	// console.log(img);
	});
	
	function reads(fil) {
	var reader = new FileReader();
	reader.readAsDataURL(fil);	 
	reader.onload = function() {
	document.getElementById("uploadBox").innerHTML += "<div class='divImg' id='uploadImg'><img src='" + reader.result + "' class='imgBiMG'></div>";
	}
	}
})

document.getElementById("submit").onclick = function(){
    var title = document.getElementById('title').value;
    var content = document.getElementsByClassName('my_content')[0].innerHTML;
    var come_from = document.getElementsByClassName('come_from')[0].innerHTML;
    var category = document.getElementById('category').value;
    var year = document.getElementById('year').value;
    if(title == ''){
        tips.innerHTML = "标题不能为空"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    if(content == ''){
        tips.innerHTML = "内容不能为空"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    if(come_from == ''){
        tips.innerHTML = "出处不能为空"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    if(category == ''){
        tips.innerHTML = "标签不能为空"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    if(year == ''){
        tips.innerHTML = "年份不能为空"
        tips.setAttribute('style', 'visibility: visible')
        return
    }
    var username = localStorage.getItem('username')
    let formData = new FormData();
    for(i = 0; i < img.length; i++) formData.append('image', img[i]);
    formData.append('stem', title),
    formData.append('content', content);
    formData.append('come_from', come_from);
    formData.append('category', category);
    formData.append('year', year);
    formData.append('username', username),
    axios({
        enctype:"multipart/form-data",
        type: 'json',
        method: 'post',
        url: 'http://www.lijunxi.site:1234/stem/userSaveStem',
        data: formData
    }).then(function (resp) {
        if(resp.data.data == 'ok'){
            window.location.href = 'index.html'
        }
    });
    
 }
 
 document.getElementById("my_clear").onclick = function(){
    document.getElementById('title').value = ""
    document.getElementsByClassName('my_content')[0].innerHTML = ""
    document.getElementsByClassName('come_from')[0].innerHTML = ""
    document.getElementById('category').value = ""
    document.getElementById('year').value = ""
 }

