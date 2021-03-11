/**
 * Created by shaoning on 2018/3/28.
 */
 function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg); //匹配目标参数
    if (r != null) return unescape(r[2]); return null; //返回参数值
}
function discussInit(){
    $.post("/selfPart/getAllDiscuss",{"codeSecondNumber":getUrlParam("codeManageSecondNumber")},function(getAllDiscuss){
        // console.log(getAllDiscuss["getCurrentLoginUserID"])
        var getAllDiscussToHTMLString = ""
        $.each(getAllDiscuss["getAllDiscuss"],function(index,getOneDiscuss){
            getAllDiscussToHTMLString += '<div class="discussShowOne">'
            getAllDiscussToHTMLString += '<div class="discussShowUser">'
            getAllDiscussToHTMLString += '<img class="discussShowUserImg" src="'+getOneDiscuss["CreateImg"]+'"></img>'
            getAllDiscussToHTMLString += '<a href="/otherPart/?userID='+getOneDiscuss["CreateID"]+'">'
            getAllDiscussToHTMLString += '<div class="discussShowUserName" id="discussShowUserName_'+getOneDiscuss["CreateID"]+'">'+getOneDiscuss["CreateName"]
            getAllDiscussToHTMLString += '</div></a>'
            getAllDiscussToHTMLString += '<div class="discussShowCreateDataTime">'+getOneDiscuss["CreateDataTime"]+'</div>'
            getAllDiscussToHTMLString += '<div class="discussShowReplyShowButton" id="replyShowButon_'+getOneDiscuss["CreateID"]+'">回复</div>'
            getAllDiscussToHTMLString += '</div>'
            getAllDiscussToHTMLString += '<div class="discussContent">'
            if (getOneDiscuss["ReplyID"]!="0") {
                getAllDiscussToHTMLString += '<span>回复@<a href="/otherPart/?userID='+getOneDiscuss["ReplyID"]+'" class="discussShowUserNameForReply">'+getOneDiscuss["ReplyName"]+'</a></span>：'
            };
            getAllDiscussToHTMLString += getOneDiscuss["Content"]
            getAllDiscussToHTMLString += '</div>'
            getAllDiscussToHTMLString += '</div>'
        })
        getAllDiscussToHTMLString += '<div class="discussInput" contenteditable="true"></div>'
        getAllDiscussToHTMLString += '<div class="discussOneSubmit" id="discussOneSubmit_'+getAllDiscuss["getCurrentLoginUserID"]+'">发表</div>'
        getAllDiscussToHTMLString += '<span class="discussInputReplyToUserName" id="replyToUserID_0"></span>'
        getAllDiscussToHTMLString += '<div style="width:100%;height:100px;"></div>'
        $("#discussShow").empty().append(getAllDiscussToHTMLString)
        discussClickInit()
    })
}
discussInit()
function discussClickInit(){
    $(".discussShowReplyShowButton").unbind().click(function(){
        getThisClickUserID = $(this).attr("id").split("_")[1]
        getThisClickUserName = $("#discussShowUserName_"+getThisClickUserID).text()
        $(".discussInputReplyToUserName").text("@"+getThisClickUserName+"：").attr("id","replyToUserID_"+getThisClickUserID)
        $(".discussInput").text("").focus()
        $("html").stop().animate({scrollTop:$(".discussInput").offset().top},"slow")
    })
     $(".discussInputReplyToUserName").unbind().click(function(){
        $(this).text("").attr("id","replyToUserID_0")
        $(".discussInput").text("")
     })
     $(".discussOneSubmit").unbind().click(function(){
        var oneDiscussContent = $(".discussInput").text()
        if (oneDiscussContent == "") {
            alert("评论不可为空")
            return
        };
        var discussCreateID = $(this).attr("id").split("_")[1]
        var discussReplyID = $(".discussInputReplyToUserName").attr("id").split("_")[1]
        var discussSecondNumber = getUrlParam("codeManageSecondNumber")
        $.post("/selfPart/getAllDiscussForWriteToDB",{
            "oneDiscussContent":oneDiscussContent,
            "discussCreateID":discussCreateID,
            "discussReplyID":discussReplyID,
            "discussSecondNumber":discussSecondNumber
        },function(getResult){
            if (getResult=="ok") {
                discussInit()
            }else{
                alert("登录之后才可以发表评论")
                $(".discussInput").text("")
            }
        })
     })
}