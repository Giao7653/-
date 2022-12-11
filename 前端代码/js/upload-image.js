// $(function() {
// 	var img = []; //创建一个空对象用来保存传入的图片
// 	var AllowImgFileSize = '101376'; //1兆
// 	$("#inputs").change(function() {
// 	var fil = this.files;
// 	for(var i = 0; i < fil.length; i++) {
// 	var curr = $('#inputs')[i].files[0].size;
// 	if(curr > AllowImgFileSize * 101376) { //当图片大于1兆提示
// 	layer.msg("图片文件大小超过限制 请上传小于99M的文件");
// 	} else {
// 	reads(fil[i]);
// 	img.push($('#inputs')[i].files[0]); //将传入的图片push到空对象中
// 	}
// 	}
// 	if(img.length >= 6) { //判断图片的数量，数量不能超过3张
// 	$('.uploadDIv').hide();
// 	} else {
// 	$('.uploadDIv').show();
// 	}
// 	// console.log(img);
// 	});
	
// 	function reads(fil) {
// 	var reader = new FileReader();
// 	reader.readAsDataURL(fil);	 
// 	reader.onload = function() {
// 	document.getElementById("uploadBox").innerHTML += "<div class='divImg' id='uploadImg'><img src='" + reader.result + "' class='imgBiMG'></div>";
// 	}
// 	}
// 	})

