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
        })
        $(".top_titleLink_title").css({
            "letter-spacing":"20px"
        })
        $(".top_titleLink_button").css({
            "width":"70px"
        })
    }else{
        $(".top_titleLink").css({
            "top": "0px",
            "position": "relative"
        })
        $(".top_titleLink_title").css({
            "letter-spacing":"0px"
        })
        $(".top_titleLink_button").css({
            "width":"100px"
        })
    }

    //console.log("set")
}
function outlog(){
    //console.log(i+"："+$(window).height()+"+++"+$(window).width())
    console.log($(document).scrollTop())
    if($(document).scrollTop()>30){
        setTitleShow(1)
    }else{
        setTitleShow(0)
    }
}
setInterval(outlog,10);

