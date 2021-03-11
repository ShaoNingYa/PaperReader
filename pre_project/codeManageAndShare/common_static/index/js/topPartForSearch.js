/**
 * Created by shaoning on 2018/3/29.
 */
//  function loadScript(url, callback) {
//   var script = document.createElement("script");
//   script.type = "text/javascript";
//   if(typeof(callback) != "undefined"){
//     if (script.readyState) {
//       script.onreadystatechange = function () {
//         if (script.readyState == "loaded" || script.readyState == "complete") {
//           script.onreadystatechange = null;
//           callback();
//         }
//       };
//     } else {
//       script.onload = function () {
//         callback();
//       };
//     }
//   }
//   script.src = url;
//   document.body.appendChild(script);
// }

// loadScript("/static/index/js/jquery-3.2.1.js");

// $("#search_input").change(function(){
//     console.log(111)
// })
var currentChoice=0
$("body").append('<link rel="stylesheet" type="text/css" href="/static/index/css/topPartForSearch.css">')
$("body").append('<link rel="stylesheet" href="/static/index/css/scroll.css"/>')
$("#top_titleLink_button_search").append('<div id="searchGetResult" class="scrollForSearch"></div>')
$("#search_input").focus(function(){
    $(this).next().css({"display":"none"})
    $("#searchGetResult").empty().css({"opacity":"1"})
    currentChoice=0
}).on('input propertychange', function() {
    currentChoice=0
    $("#searchGetResult").empty()
    var keywords = $(this).val()
    if (keywords!="") {
        $.post("/index/topSearchByAjaxGetResult",{"keywords":keywords},function(searchResult){
            // console.log(searchResult["codeInfoAll"])
            var searchResult_user=searchResult["userInfoAll"]
            var searchResult_code=searchResult["codeInfoAll"]
            var searchResult_tag=searchResult["tagInfoAll"]
            var currentGetResultUserID = 0
            var currentGetResultCodeName = ""
            $.each(searchResult_user,function(index,resultOneUser){
                // console.log(resultOneUser)
                if (currentGetResultUserID!=resultOneUser["userID"]) {
                    $("#searchGetResult").append('<a href="/otherPart/?userID='+resultOneUser["userID"]+'" title="'+resultOneUser["userName"]+'"><div class="searchResultOne">用户：'+resultOneUser["userName"]+'</div></a>')
                    currentGetResultUserID=resultOneUser["userID"]
                };
                $("#searchGetResult").append('<div class="searchResultOneReason">'+resultOneUser["getReason"]+'</div>')
            })
            $.each(searchResult_code,function(index,resultOneCode){
                // console.log(resultOneCode)
                if (currentGetResultCodeName!=resultOneCode["codeFirstNumber"]) {
                    $("#searchGetResult").append('<a href="/selfPart/codeOneProject?codeManageFirstNumber='+resultOneCode["codeFirstNumber"]+'" title="'+resultOneCode["codeName"]+'"><div class="searchResultOne">程序：'+resultOneCode["codeName"]+'</div></a>')
                    currentGetResultCodeName=resultOneCode["codeFirstNumber"]
                };
                $("#searchGetResult").append('<div class="searchResultOneReason">'+resultOneCode["getReason"]+'</div>')
            })
            $.each(searchResult_tag,function(index,resultOneTag){
                // console.log(resultOneCode)
                $("#searchGetResult").append('<a href="/index?tag=codeTag_'+resultOneTag["tagID"]+'"><div class="searchResultOne">标签：'+resultOneTag["tagName"]+'</div></a>')
                // $("#searchGetResult").append('<div class="searchResultOneReason">'+resultOneTag["getReason"]+'</div>')
            })
            $(".searchResultOne").eq(currentChoice).addClass("searchResultOneBeChoice")
        })
    };
}).blur(function(){
    $(this).next().css({"display":"inline"})
    $(this).val("")
    currentChoice=0
    $("#searchGetResult").css({"opacity":"0"})
}).click(function(){
    event.stopPropagation();
}).keydown(function(e){
    // console.log(e)
    if (e.key=="ArrowDown") {
        //箭头下移
        if (currentChoice<$(".searchResultOne").length-1) {
            currentChoice+=1
        }else{
            currentChoice=0
        };
        $(".searchResultOneBeChoice").removeClass("searchResultOneBeChoice")
        $(".searchResultOne").eq(currentChoice).addClass("searchResultOneBeChoice")
        // console.log($(".searchResultOne").eq(currentChoice))
        moveScrollAuto()
    }else if (e.key=="ArrowUp") {
        //箭头上移
        event.preventDefault()//控制光标保持原样
        if (currentChoice>0) {
            currentChoice-=1
        }else{
            currentChoice=$(".searchResultOne").length-1
        };
        $(".searchResultOneBeChoice").removeClass("searchResultOneBeChoice")
        $(".searchResultOne").eq(currentChoice).addClass("searchResultOneBeChoice")
        moveScrollAuto()
    }else if (e.key=="Enter") {
        //回车
        console.log(currentChoice)
        $(".searchResultOneBeChoice").click()
    }else if (e.key=="Escape") {
        //取消搜索
        $(this).blur()
    };
}).attr("placeholder","在这里输入")

function moveScrollAuto(){
    var getScrollTop = $("#searchGetResult").scrollTop()
    console.log($("#searchGetResult"))
    if ($(".searchResultOne").length==currentChoice+1) {
        // $("#searchGetResult").scrollTop(520)
        $("#searchGetResult").stop().animate({
            scrollTop: 520
        }, 500);
    }else{
        // $("#searchGetResult").scrollTop(520*currentChoice/$(".searchResultOne").length)
        $("#searchGetResult").stop().animate({
            scrollTop: 520*currentChoice/$(".searchResultOne").length
        }, 500);
    }
}