/**
 * Created by shaoning on 2018/4/11.
 */
    //mainShowBodyControlNewInf
    //mainShowBodyControlCodeManageChoice
    //mainShowBodyControlSelfSet

function removeMainShowBodyShowFlag(){
    $("#mainShowBodyControlNewInfChoice").removeClass("mainShowBodyControlChoiceIs").addClass("mainShowBodyControlChoice");
    $("#mainShowBodyControlCodeManageChoice").removeClass("mainShowBodyControlChoiceIs").addClass("mainShowBodyControlChoice");
    $("#mainShowBodyControlSelfSetChoice").removeClass("mainShowBodyControlChoiceIs").addClass("mainShowBodyControlChoice");
    $("#mainShowBodyControlNewInf").stop().slideUp(150);
    $("#mainShowBodyShowCodeManage").stop().slideUp(150);
    $("#mainShowBodyControlSelfSet").stop().slideUp(150);
}
var mainShowBodyShowFlag=0;
$("#mainShowBodyControlNewInfChoice").click(function(){
    if(mainShowBodyShowFlag!=0){
        removeMainShowBodyShowFlag();
        $(this).removeClass("mainShowBodyControlChoice").addClass("mainShowBodyControlChoiceIs");
        $("#mainShowBodyControlNewInf").slideDown(800);
        console.log("change");
        mainShowBodyShowFlag=0
    }
});
var mainShowBodyControlNewInfAllContentShowChoiceFlag=0;
$("#mainShowBodyControlNewInfAllContentShowChoiceAll").click(function(){//显示所有
    if(mainShowBodyControlNewInfAllContentShowChoiceFlag==1){
        $(this).addClass("mainShowBodyControlNewInfAllContentShowChoiceIs").removeClass("mainShowBodyControlNewInfAllContentShowChoiceNo");
        $("#mainShowBodyControlNewInfAllContentShowChoiceSelf").addClass("mainShowBodyControlNewInfAllContentShowChoiceNo").removeClass("mainShowBodyControlNewInfAllContentShowChoiceIs");
        $(".mainShowBodyControlNewInfAllContentAll").slideDown(0);
        $(".mainShowBodyControlNewInfAllContentSelf").slideUp(0);
        mainShowBodyControlNewInfAllContentShowChoiceFlag=0
    }
});
$("#mainShowBodyControlNewInfAllContentShowChoiceSelf").click(function(){//仅显示个人
    if(mainShowBodyControlNewInfAllContentShowChoiceFlag==0){
        $(this).addClass("mainShowBodyControlNewInfAllContentShowChoiceIs").removeClass("mainShowBodyControlNewInfAllContentShowChoiceNo");
        $("#mainShowBodyControlNewInfAllContentShowChoiceAll").addClass("mainShowBodyControlNewInfAllContentShowChoiceNo").removeClass("mainShowBodyControlNewInfAllContentShowChoiceIs");
        $(".mainShowBodyControlNewInfAllContentAll").slideUp(0);
        $(".mainShowBodyControlNewInfAllContentSelf").slideDown(0);
        mainShowBodyControlNewInfAllContentShowChoiceFlag=1
    }
});
$("#mainShowBodyControlCodeManageChoice").click(function(){
    if(mainShowBodyShowFlag!=1){
        removeMainShowBodyShowFlag();
        $(this).removeClass("mainShowBodyControlChoice").addClass("mainShowBodyControlChoiceIs");
        $("#mainShowBodyShowCodeManage").slideDown(800);
        console.log("change");
        mainShowBodyShowFlag=1
    }
});
$("#mainShowBodyControlSelfSetChoice").click(function(){
    if(mainShowBodyShowFlag!=2){
        removeMainShowBodyShowFlag();
        $(this).removeClass("mainShowBodyControlChoice").addClass("mainShowBodyControlChoiceIs");
        $("#mainShowBodyControlSelfSet").slideDown(500);
        console.log("change");
        mainShowBodyShowFlag=2
    }
});