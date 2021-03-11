/**
 * Created by 邵宁 on 2017/11/26 0026.
 */
var i=0;
//setTimeout("i+=1;alert(i)",1000);
function setTitleShow(get){
    if(get==1){
        $(".top_titleLink").css({
            "top": "0px",
            "position": "fixed"
        });
        $(".top_titleLink_title").css({
            "letter-spacing":"20px"
        });
        $(".top_titleLink_button").css({
            "width":"70px"
        });
        $("#search_input").css({
            "display":"none"
        });
    }else{
        $(".top_titleLink").css({
            "top": "0px",
            "position": "relative"
        });
        $(".top_titleLink_title").css({
            "letter-spacing":"0px"
        });
        $(".top_titleLink_button").css({
            "width":"100px"
        });
        $("#search_input").css({
            "display":"none"
        });
    }

    //console.log("set")
}
var a=0;
var b=a;
function outlog(){
    //console.log(i+"："+$(window).height()+"+++"+$(window).width())
    //console.log($(document).scrollTop())

    if($(document).scrollTop()>30){
        a=1
    }else{
        a=0
    }
    if(b!=a){
        setTitleShow(a);
        b=a;
        // console.log($(document).scrollTop())
    }
    changeMoveToFlagClass()
}
setInterval(outlog,10);
 // document.onmousewheel=function(e){
 //        console.log("鼠标滚动事件")
 //        if (lastScrollHeight>$(document).scrollTop()) {
 //            console.log("up")
 //            moveToNextScreen($(document).scrollTop(),"up")
 //            lastScrollHeight=$(document).scrollTop()
 //        }else if (lastScrollHeight<$(document).scrollTop()) {
 //            console.log("down")
 //            moveToNextScreen($(document).scrollTop(),"down")
 //            lastScrollHeight=$(document).scrollTop()
 //        }
 //    }


$(document).ready(function(){
    $("#top_titleLink_button_search").click(function(){
        $("#top_titleLink_button_search").css({
            "width":"300px"
        }).ready(function(){
            $("#search_input").css({
                "display":"block"
            });
            $("#search_input")[0].focus()
        })
    });
    $("#top_titleLink_button_search").focusout(function(){
        $("#top_titleLink_button_search").css({
            "width":"100px"
        });
        $("#search_input").css({
            "display":"none"
        })
    })
});
$.get("/allUser/allPartCodeSelectAndShow",function(getHtmlForCodeSelectAndShow){
    // console.log(getHtmlForCodeSelectAndShow)
    getHtmlForCodeSelectAndShow += '<div style="width:100%;height:100px;"></div>'
    $("#codeSelectAndShowForIndex").append(getHtmlForCodeSelectAndShow)
    setTimeout(function(){
        if (getUrlParam("tag")) {
            // console.log(getUrlParam("tag"))
            $("#moveToFlag_3").click()
            $("#"+getUrlParam("tag")).click()
        };
    }, 500);
})

// 下面是实现点击按钮滚动一屏幕
$(".moveToFlagClass").click(function(){
    getID=$(this).attr("id").split("_")[1]
    heightForThisFlag=$("#flag_"+getID).offset().top
    $("html").stop().animate({scrollTop:heightForThisFlag-70},"slow");
})
var lastScreenFlag=0
var screenFlagHeight_2=$("#flag_2").offset().top-140
var screenFlagHeight_3=$("#flag_3").offset().top-160
function changeMoveToFlagClass(){
    var currentDocumentHeight = $(document).scrollTop()
    if (currentDocumentHeight<screenFlagHeight_2) {
        if (lastScreenFlag!=1) {
            $(".moveToFlagClassIs").removeClass("moveToFlagClassIs")
            $("#moveToFlag_1").addClass("moveToFlagClassIs")
            lastScreenFlag=1
        };
    }else if (currentDocumentHeight>screenFlagHeight_2 && currentDocumentHeight<screenFlagHeight_3) {
        if (lastScreenFlag!=2) {
            $(".moveToFlagClassIs").removeClass("moveToFlagClassIs")
            $("#moveToFlag_2").addClass("moveToFlagClassIs")
            lastScreenFlag=2
        }
    }else if (currentDocumentHeight>screenFlagHeight_3) {
        if (lastScreenFlag!=3) {
            $(".moveToFlagClassIs").removeClass("moveToFlagClassIs")
            $("#moveToFlag_3").addClass("moveToFlagClassIs")
            lastScreenFlag=3
        }
    };
}
function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg); //匹配目标参数
    if (r != null) return unescape(r[2]); return null; //返回参数值
}
