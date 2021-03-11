/**
 * Created by shaoning on 2018/4/16.
 */
$("#changePassword").click(function(){
    $("#changePasswordWindowHidden").slideDown(150);
    $("html").css({
        "overflow":"hidden"
    });
    $("#changePasswordWindowNewPassword").val("")
    $("#changePasswordWindowOldPassword").val("").focus()
});
function changePasswordCancel(){
    console.log(111);
    $("#changePasswordWindowHidden").slideUp(150);
    $("html").css({
        "overflow":"auto"
    })
}
$("#changePasswordWindow").click(function(){
    event.stopPropagation();
});
$("#changePasswordWindowHidden").click(function(){
    changePasswordCancel();
});
$("#changePasswordWindowNo").click(function(){
    changePasswordCancel();
});
$("#changePasswordWindowYes").click(function(){
    var oldPassword = $("#changePasswordWindowOldPassword").val()
    var newPassword = $("#changePasswordWindowNewPassword").val()
    if (oldPassword == "") {
        alert("旧密码不可为空")
        $("#changePasswordWindowOldPassword").focus()
        return false
    };
    if (newPassword == "") {
        alert("新密码不可为空")
        $("#changePasswordWindowNewPassword").focus()
        return false
    };
    if (oldPassword == newPassword) {
        alert("新旧密码不可相同")
        $("#changePasswordWindowNewPassword").focus()
        return false
    };
    $.post("/selfPart/changePassword",{'oldPassword':oldPassword,"newPassword":newPassword},function(changeResult){
        alert(changeResult)
        if (changeResult == "修改成功") {
            window.location.href='/login'; 
        };
    });
    changePasswordCancel();
});