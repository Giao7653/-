document.getElementById("search").onclick = function(){
    var $searchStem = $('#searchStem').val();
    if ($searchStem == "") {
        alert("搜索不能为空");
        return;
    }
    window.location.href="search.html?stem=" + $searchStem;
}

document.getElementById("clear_history").onclick = function(){
   localStorage.removeItem('search_data');
   $(".my_search").load(location.href + " .my_search");
   
}

document.getElementById("create").onclick = function(){
   if(localStorage.getItem('username') == null || localStorage.getItem('token') == null){
        alert('请先登录')
        return
   }
   window.location.href="addstem.html"
 }