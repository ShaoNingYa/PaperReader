///**
// * Created by shaoning on 2018/3/14.
// */
//var obox = document.getElementById("rightClickContent");
///*点击鼠标右键时执行*/
////document.oncontextmenu =  function(ev){
////    var e = ev||window.event;
////    var x = e.clientX;
////    var y = e.clientY;
////    obox.style.cssText = "display:block;top:"+y+"px;left:"+x+"px;height:200px;";
////    return false;
////};
/////*点击空白处隐藏*/
////document.onclick = function(){
////    obox.fadeOut(1000);
////    //obox.style.cssText = "height:0px;";
////    //obox.style.display = "none";
////};
//
//document.oncontextmenu =  function(ev){
//    var e = ev||window.event;
//    var x = e.clientX;
//    var y = e.clientY;
//    obox.style.cssText = "top:"+y+"px;left:"+x+"px;height:200px;";
//    //$("#rightClickContent").show(100);
//    $("#rightClickContent").slideToggle("normal");
//    return false;
//};
/////*点击空白处隐藏*/
////document.onclick = function(){
////    $("#rightClickContent").hide();
////    //obox.style.cssText = "height:0px;";
////    //obox.style.display = "none";
////};
////
////$("#rightClickContentText01").click(function(){
////    alert(1)
////});
////$("#rightClickContentText02").click(function(){
////    alert(2)
////});
////
////$("#rightClickContentText05").click(function(){
////    window.location.reload()
////});
//
//$(".mainShowBodyShowMessageStyle_FriendPersonOne").mousedown(function(e) {
//    console.log(e.which);
//    //右键为3
//    if (3 == e.which) {
//        $(this).css({
//            "font-size": "-=2px"
//        });
//        var e = e||window.event;
//        var x = e.clientX;
//        var y = e.clientY;
//        obox.style.cssText = "top:"+y+"px;left:"+x+"px;height:200px;";
//        //$("#rightClickContent").show(100);
//        $("#rightClickContent").slideToggle("normal");
//        return false
//    } else if (1 == e.which) {
//        //左键为1
//        $(this).css({
//            "font-size": "+=3px"
//        });
//    }
//});
var kyoPopupMenu={};
kyoPopupMenu = (function(){
    return {
        sys: function (getId) {
            console.log(getId);
            $('.popup_menu').remove();
            popupMenuApp = $('<div class="popup_menu app-menu"><ul><li><a menu="menu1">发送消息</a></li><li><a menu="menu2">查看资料</a></li><li><a menu="menu3">删除朋友</a></li></ul></div>')
                .find('a').attr('href','javascript:;')
                .end().appendTo('body');
            //绑定事件
            $('.app-menu a[menu="menu1"]').on('click', function (){
                console.log($(getId).text());
                $("#mainShowBodyShowMessageStyleSelect_Communicate").click();
                if($("#"+getId.id.split("_")[1]).length>0){
                    $("#"+getId.id.split("_")[1]).click()
                }else{
                    var newCommunicateOne='<div class="mainShowBodyShowMessageStyle_CommunicatePersonOne " id="'+getId.id.split("_")[1]+'"><img src="1.png" alt="" class="mainShowBodyShowMessageStyle_CommunicatePersonOnePic"/><div class="mainShowBodyShowMessageStyle_CommunicatePersonOneName">'+$(getId).text()+'</div></div>';
                    $("#mainShowBodyShowMessageStyle_CommunicatePerson").prepend(newCommunicateOne);
                    var newCommunicateOneWindow='<div class="mainShowBodyShowMessageStyle_CommunicateWindow" id="message_'+getId.id.split("_")[1]+'">'+
                        '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTitle">'+$(getId).text()+'</div>'+
                        '<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalk scrollStyle">'+
                        //'<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMe">'+
                        //'<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUser">邵宁 <span class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUserTime">2018/4/18 14:46:16</span></div>'+
                        //'<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMessage">啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦</div>'+
                        //'</div>'+
                        //'<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkHe">'+
                        //'<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkHeUser">郑仲 <span class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMeUserTime">2018/4/18 14:46:16</span></div>'+
                        //'<div class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMessage">啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦</div>'+
                        //'</div>'+
                        '</div>'+
                        '<div class="mainShowBodyShowMessageStyle_CommunicateWindowInput scrollStyle" contenteditable="true" id="input_'+getId.id.split("_")[1]+'">在这里输入内容</div>'+
                        '<input type="button" value="发送" class="mainShowBodyShowMessageStyle_CommunicateWindowTalkMessageSend" id="send_'+getId.id.split("_")[1]+'"/>'+
                        '</div>';
                    $("#mainShowBodyShowMessageStyle_Communicate").append(newCommunicateOneWindow);

                    /******添加完元素之后要重新进行初始化****下边****/
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
                    /******添加完元素之后要重新进行初始化****上边****/
                    $("#"+getId.id.split("_")[1]).click()
                }
            });
            $('.app-menu a[menu="menu2"]').on('click', function (){
                console.log(getId)
            });
            $('.app-menu a[menu="menu3"]').on('click', function (){
                console.log(getId)
            });
            return popupMenuApp;
        }
    }})();
//取消右键
$('html').on('contextmenu', function (){return true;}).click(function(){
    $('.popup_menu').hide();
});
//桌面点击右击
$('.mainShowBodyShowMessageStyle_FriendPersonOne').on('contextmenu',function (e){
    //console.log(this.id);
    var popupmenu = kyoPopupMenu.sys(this);
    l = ($(document).width() - e.clientX) < popupmenu.width() ? (e.clientX - popupmenu.width()) : e.clientX;
    t = ($(document).height() - e.clientY) < popupmenu.height() ? (e.clientY - popupmenu.height()) : e.clientY;
    popupmenu.css({left: l,top: t+$(window).scrollTop()}).slideDown(1000);
    return false;
});