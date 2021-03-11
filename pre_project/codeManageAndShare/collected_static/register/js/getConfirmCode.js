/**
 * Created by shaoning on 2018/3/28.
 */
$("#RegGetConfirm").click(function () {
    var confirmEmail=$("#regEmail").val();
    if (confirmEmail == "") {
        alert("请输入邮箱")
        $("#regEmail").focus()
    }else{
        if($("#regPassword").val() == ""){
            alert("密码不可为空")
            $("#regPassword").focus()
        }else{
            var reg = /\w+[@]{1}\w+[.]\w+/;
            if (reg.test(confirmEmail)) {
                $("#RegGetConfirm").attr({"disabled":"disabled","value":"一次性使用"});
                $("#regConfirm").removeAttr("disabled").focus().keydown(function(){
                    if(event.keyCode == 13){
                        //alert("提交")
                        if($(this).val().length==6){
                            $("#regSubmit").click()
                        }
                    }
                });
                var regEmailFocusFlag=0;
                $("#regEmail").focus(function(){
                    if(regEmailFocusFlag==0)alert("不要随意更改邮箱");
                    regEmailFocusFlag=1
                });
                $.get("/ajax_sendEmail/",{'conFirmEmail':confirmEmail},function(isSend){
                    $("#RegGetConfirm").attr({"disabled":"disabled","value":isSend});
                });
                //alert("email合法");
            } else {
                alert("请输入正确的email地址");
                $("#regEmail").focus()
            }
        }
    }
});
//$("#regConfirm").change(function(){
//   console.log($(this).val())
//});
$("#regConfirm").on('input',function(e){
    console.log($(this).val().length);
    if($(this).val().length==6){
        $("#regSubmit").removeAttr("disabled").css({
            "background-color":"rgba(2, 117, 216, 0.6)",
            "color":"rgba(255, 255, 255, 0.98)",
            "box-shadow":"0 0 15px rgba(52, 48, 71, 0.56)",
            "border-radius":"15px",
            "cursor":"pointer"
            //"opacity":"0.6"
        })
    }else{
        $("#regSubmit").attr("disabled","disabled").css({
            "background-color":"rgba(167, 172, 181, 0.11)",
            "color":"rgb(131, 122, 122)",
            "box-shadow":"none",
            "border-radius":"0",
            "cursor":"wait"
            //"opacity":"0.4"
        })
    }
});

$("#regSubmit").mousedown(function(){
    $(this).css("box-shadow"," none")
}).mouseup(function(){
}).click(function(){
    //alert(111)
    $(this).css({
        "background-color":"rgba(135, 255, 96, 0.8)",
        "color":"rgba(255, 255, 255, 0.98)",
        "box-shadow":"none",
        "border-radius":"0"
    })
    enterRegisterPart2();
}).mouseleave(function () {
    $(this).css({
        "background-color":"rgba(2, 117, 216, 0.6)",
        "color":"rgba(255, 255, 255, 0.98)",
        "box-shadow":"0 0 15px rgba(52, 48, 71, 0.56)",
        "border-radius":"15px"
        //"opacity":"0.9"
    })
}).mouseenter(function(){
    $(this).css({
        "background-color":"rgba(2, 117, 216, 0.3)",
        "color":"rgba(255, 255, 255, 0.8)",
        "box-shadow":"0 0 10px rgba(52, 48, 71, 0.8)",
        "border-radius":"20px",
        "cursor":"pointer"
        //"opacity":"0.6"
    })
});
