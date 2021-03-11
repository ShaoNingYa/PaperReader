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
        console.log($(document).scrollTop())
    }

}
setInterval(outlog,10);


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