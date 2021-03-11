/**
 * Created by shaoning on 2018/5/11.
 */
$(".mainShowTitleShowRightBarChoice").click(function(){
    var manageType = $(this).attr("id").split("_")[0]
    var currentLoginUserID = $(this).attr("id").split("_")[1]
    var currentCheckUserID = $(this).attr("id").split("_")[2]
    if (manageType == "addFriend") {
        $.post("otherPart/addFriend",{"currentLoginUserID":currentLoginUserID,"currentCheckUserID":currentCheckUserID},function(){
             window.location.reload();
        })
    }else if (manageType == "delFriend") {
        $.post("otherPart/delFriend",{"currentLoginUserID":currentLoginUserID,"currentCheckUserID":currentCheckUserID},function(){
             window.location.reload();
        })
    }else if (manageType == "addFocus") {
        $.post("otherPart/addFocus",{"currentLoginUserID":currentLoginUserID,"currentCheckUserID":currentCheckUserID},function(){
             window.location.reload();
        })
    }else if (manageType == "delFocus") {
        $.post("otherPart/delFocus",{"currentLoginUserID":currentLoginUserID,"currentCheckUserID":currentCheckUserID},function(){
             window.location.reload();
        })
    }
})