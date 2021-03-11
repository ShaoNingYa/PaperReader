/**
 * Created by shaoning on 2018/3/28.
 */
var loginUser = $("#loginUser");
var loginPassword = $("#loginPassword");

$("#loginConfirm").click(function () {


});

loginPassword.keydown(function () {
    if (event.keyCode == 13) {
        //alert("提交")
        console.log("回车");
        $("#loginSubmit").click()
    }
}).on('input', function (e) {
    console.log($(this).val().length);
    if ($(this).val().length > 0) {
        $("#loginSubmit").removeAttr("disabled").css({
            "background-color": "rgba(2, 117, 216, "+$(this).val().length*0.1+")",
            "color": "rgba(255, 255, 255, 0.98)",
            "box-shadow": "0 0 15px rgba(52, 48, 71, 0.56)",
            "border-radius": "15px",
            "cursor": "pointer"
            //"opacity":"0.6"
        })
    } else {
        $("#loginSubmit").attr("disabled", "disabled").css({
            "background-color": "rgba(167, 172, 181, 0.11)",
            "color": "rgb(131, 122, 122)",
            "box-shadow": "none",
            "border-radius": "0",
            "cursor": "wait"
            //"opacity":"0.4"
        })
    }
});

$("#loginSubmit").mousedown(function () {
    $(this).css("box-shadow", " none")
}).mouseup(function () {
}).click(function () {

    if (loginUser.val() == "") {
        alert("账户不可为空");
        loginUser.focus()
    } else {
        if (loginPassword.val() == "") {
            alert("密码不可为空");
            loginPassword.focus()
        } else {
            //if () {//进行验证码验证
            //console.log("验证码通过");
                $.post("/login/",{"username":loginUser.val(),"password":loginPassword.val()},function(result){
                console.log("通过");
                $(this).css({
                    "background-color": "rgba(135, 255, 96, 0.8)",
                    "color": "rgba(255, 255, 255, 0.98)",
                    "box-shadow": "none",
                    "border-radius": "0"
                });
                window.location.href='/selfPart';
            });
            //console.log("通过");
            //$(this).css({
            //    "background-color": "rgba(135, 255, 96, 0.8)",
            //    "color": "rgba(255, 255, 255, 0.98)",
            //    "box-shadow": "none",
            //    "border-radius": "0"
            //})
            //接下来进行后台密码验证
            //}
        }
    }
}).mouseleave(function () {
    $(this).css({
        "background-color": "rgba(2, 117, 216, "+$("#loginPassword").val().length*0.1+")",
        "color": "rgba(255, 255, 255, 0.98)",
        "box-shadow": "0 0 15px rgba(52, 48, 71, 0.56)",
        "border-radius": "15px",
        "cursor": "pointer"
        //"opacity":"0.9"
    })
}).mouseenter(function () {
    $(this).css({
        "background-color": "rgba(2, 117, 216, 0.3)",
        "color": "rgba(255, 255, 255, 0.8)",
        "box-shadow": "0 0 10px rgba(52, 48, 71, 0.8)",
        "border-radius": "30px",
        "cursor": "pointer"
        //"opacity":"0.6"
    })
});
