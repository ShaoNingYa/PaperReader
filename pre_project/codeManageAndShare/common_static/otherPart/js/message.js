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
    $.post("/selfPart/messageRemoveNewOne",{"getAlreadyReadNumber":this.id});
    $(this).addClass("mainShowBodyShowMessageStyle_CommunicatePersonOneBeChoice").removeClass("mainShowBodyShowMessageStyle_CommunicatePersonOneHaveNew");
    console.log($(this).text());
    $(".mainShowBodyShowMessageStyle_CommunicateWindow").slideUp(0);
    var willPushID = "#message_"+this.id;
    $(willPushID).slideDown(0);
    /********获取消息********/
    var CurrentUserName=$(this).text();
    $.get("/selfPart/getOneMessage",{'studyNumber':this.id},function(oneMessages){
        //var oneMessages = [[1,2,"a","2018-04-21 05:30:20"],[2,1,"b","2018-04-21 15:30:20"],2];
        var userIDCurrentUserID = oneMessages.pop();
        //[thisMessage.selfPartMessageSendUserID,thisMessage.selfPartMessageReceUserID,thisMessage.selfPartMessageContent]
        var oneMessage="";
        for( i in oneMessages){
            //console.log(oneMessages[i])
            if(oneMessages[i][0]==userIDCurrentUserID){
                oneMessage+='<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMe">'+
                '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUser"> '+$("#mainShowTitleShowRightName").text()+
                '  <span class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUserTime">'+oneMessages[i][3]+
                '</span></div>'+
                '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMessage">'+oneMessages[i][2]+
                '</div></div>'
            }else{
                oneMessage+='<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkShe">'+
                '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkSheUser">'+CurrentUserName+
                '  <span class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUserTime">'+oneMessages[i][3]+
                '</span></div>'+
                '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMessage">'+oneMessages[i][2]+
                '</div></div>'
            }
        }
        console.log(oneMessage);
        var messageWindowForGetOnePersonMessages = $(willPushID +" .mainShowBodyShowMessageStyle_CommunicateWindowTalk");
        messageWindowForGetOnePersonMessages.empty().append(oneMessage).scrollTop(messageWindowForGetOnePersonMessages[0].scrollHeight);
    });
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
    //console.log("点击发送按钮"+this.id);
    var willSendTOUserID=this.id.split("_")[1];
    var getMessage=$("#input_"+willSendTOUserID);
    if(""==getMessage.text()||"在这里输入内容"==getMessage.text()){
        alert("请输入要发送的消息")
    }else{
        var messageOnePush='<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMe">'+
            '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUser">'+$("#mainShowTitleShowRightName").text()+' <span class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUserTime">'+getTime()+'</span></div>'+
            '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMessage">'+getMessage.text()+'</div>'+
            '</div>';
        //console.log("发送信息"+willSendTOUserID);
        //console.log(messageOnePush);
        var willSendMessage = {"selfPartMessageReceUserID":willSendTOUserID,"selfPartMessageContent":getMessage.text()};
        $.post("/selfPart/messageWrite",willSendMessage,function(result){
            console.log("通过");
            var messageWindow=$("#message_"+willSendTOUserID+ " .mainShowBodyShowMessageStyle_CommunicateWindowTalk");
            messageWindow.append(messageOnePush).scrollTop(messageWindow[0].scrollHeight);
            getMessage.text("");
        });
    }
});
/*************发送消息**************up*************/
/*************定时获取最新的消息*****down**********/
setInterval(function(){
    $.post("/selfPart/messageGetNewAll",function(allMessageUserNumbers){
        // console.log("获取到所有有新消息的用户");
        // console.log(allMessageUserNumbers)
        var CurrentUserNumber = $(".mainShowBodyShowMessageStyle_CommunicatePersonOneBeChoice").attr("id")
        // console.log("当前正在聊天的用户"+CurrentUserNumber)
        for(allMessageUserNumber in allMessageUserNumbers){
            $("#"+allMessageUserNumbers[allMessageUserNumber]).addClass("mainShowBodyShowMessageStyle_CommunicatePersonOneHaveNew")
        }
        if ($.inArray(CurrentUserNumber,allMessageUserNumbers)>=0) {
            $("#"+CurrentUserNumber).click()
            // console.log("重新点击当前用户")
        };
    });
},1000);
/*************定时获取最新的消息*****up*********/