/**
 * Created by shaoning on 2018/4/18.
 */
var messageShowFlag=0;
$("#mainShowBodyShowMessageStyleSelect_Communicate").click(function(){
    if(messageShowFlag==1){
        messageShowFlag=0;
        $("#mainShowBodyShowMessageStyleSelect_Communicate").addClass("beChoice");
        $("#mainShowBodyShowMessageStyleSelect_Friend").removeClass("beChoice");
        $("#mainShowBodyShowMessageStyle_Friend").stop().slideUp(0);
        $("#mainShowBodyShowMessageStyle_Communicate").slideDown(0)
    }
});
$("#mainShowBodyShowMessageStyleSelect_Friend").click(function(){
    if(messageShowFlag==0){
        messageShowFlag=1;
        $("#mainShowBodyShowMessageStyleSelect_Friend").addClass("beChoice");
        $("#mainShowBodyShowMessageStyleSelect_Communicate").removeClass("beChoice");
        $("#mainShowBodyShowMessageStyle_Communicate").stop().slideUp(0);
        $("#mainShowBodyShowMessageStyle_Friend").slideDown(0)
    }
});
$(".mainShowBodyShowMessageStyle_CommunicatePersonOne").click(function(){
    $(".mainShowBodyShowMessageStyle_CommunicatePersonOne").removeClass("mainShowBodyShowMessageStyle_CommunicatePersonOneBeChoice");
    $(this).addClass("mainShowBodyShowMessageStyle_CommunicatePersonOneBeChoice");
    console.log($(this).text());
    $(".mainShowBodyShowMessageStyle_CommunicateWindow").slideUp(0);
    $("#message_"+this.id).slideDown(0);
});
$(".mainShowBodyShowMessageStyle_CommunicateWindowInput").blur(function(){
    if($(this).text()==""){
        $(this).text("在这里输入内容").css({
            "color":"rgba(169, 169, 169, 0.85)"
        })
    }
}).focus(function(){
    if($(this).text()=="在这里输入内容"){
        $(this).text("")
    }
    $(this).css({
        "color":"black"
    })
}).keydown(function () {
    if (event.keyCode == 13) {
        //alert("提交")
        //console.log("回车");
        //console.log("回车"+this.id);
        $("#send_"+this.id.split("_")[1]).click();
    }
});
/*************发送消息**************down*************/
function getTime(){
    function p(s) {
        return s < 10 ? '0' + s: s;
    }
    var myDate = new Date();
    //获取当前年
    var year=myDate.getFullYear();
    //获取当前月
    var month=myDate.getMonth()+1;
    //获取当前日
    var date=myDate.getDate();
    var h=myDate.getHours();       //获取当前小时数(0-23)
    var m=myDate.getMinutes();     //获取当前分钟数(0-59)
    var s=myDate.getSeconds();
    var now=year+'-'+p(month)+"-"+p(date)+" "+p(h)+':'+p(m)+":"+p(s);
    console.log(now);
    return now
}
$(".mainShowBodyShowMessageStyle_CommunicateWindowTalkMessageSend").click(function(){
    console.log(this.id);
    var getMessage=$("#input_"+this.id.split("_")[1]);
    if(""==getMessage.text()||"在这里输入内容"==getMessage.text()){
        alert("请输入要发送的消息")
    }else{
        var messageOnePush='<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMe">'+
            '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUser">邵宁 <span class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUserTime">'+getTime()+'</span></div>'+
            '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMessage">'+getMessage.text()+'</div>'+
            '</div>';
        console.log("发送信息"+this.id.split("_")[1]);
        console.log(messageOnePush);
        var messageWindow=$("#message_"+this.id.split("_")[1]+ " .mainShowBodyShowMessageStyle_CommunicateWindowTalk");
        messageWindow.append(messageOnePush).scrollTop(messageWindow[0].scrollHeight);
        getMessage.text("");
    }
});
/*************发送消息**************up*************/