/**
 * Created by shaoning on 2018/4/16.
 */
$("#changePassword").click(function(){
    $("#changePasswordWindowHidden").slideDown(150);
    $("html").css({
        "overflow":"hidden"
    });
    $("#changePasswordWindowOldPassword").focus()
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