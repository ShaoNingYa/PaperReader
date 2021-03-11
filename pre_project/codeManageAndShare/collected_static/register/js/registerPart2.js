/**
 * Created by shaoning on 2018/3/29.
 */
function enterRegisterPart2() {
    $("#registerBaseShowPart1").css({
        "display":"none"
    });
    $("#registerBaseShowPart2").css({
        "display":"block"
    });
    //在这里追加新的内容
    /*******接下来实现新的逻辑********/
    //$('#sexChoice').
    var year = new Date().getFullYear(); //获取当前年份
    //var gradeChoice = document.getElementById('gradeChoice');//获取select下拉列表
    //for (var i = year; i > year-5; i--)//循环添加2006到当前年份加3年的每个年份依次添加到下拉列表
    //{
    //    var option = document.createElement('option');
    //    option.value = i;
    //    var txt = document.createTextNode(i);
    //    option.appendChild(txt);
    //    gradeChoice.appendChild(option);
    //}
    //var classChoice = document.getElementById('classChoice');//获取select下拉列表
    //for (i = 1; i < 5; i++)//循环添加2006到当前年份加3年的每个年份依次添加到下拉列表
    //{
    //    var option = document.createElement('option');
    //    option.value = i;
    //    var txt = document.createTextNode(i);
    //    option.appendChild(txt);
    //    classChoice.appendChild(option);
    //}
    /********重写*******/
    for (var i = year; i > year - 5; i--)
        $("#gradeChoice").append('<option value=' + i + '>' + i + '</option>')
    for (i = 1; i < 6; i++)
        $("#classChoice").append('<option value=' + i + '>' + i + '</option>')

    function stateChange(){
        if($("#regStudyNumber").val().length>3 && $("#regTrueName").val()!=""){
            $("#regSubmitPart2").removeAttr("disabled").css({
                "background-color":"rgba(2, 117, 216, 0.6)",
                "color":"rgba(255, 255, 255, 0.98)",
                "box-shadow":"0 0 15px rgba(52, 48, 71, 0.56)",
                "border-radius":"15px",
                "cursor":"pointer"
                //"opacity":"0.6"
            })
        }else{
            $("#regSubmitPart2").attr("disabled","disabled").css({
                "background-color":"rgba(167, 172, 181, 0.31)",
                "color":"rgb(131, 122, 122)",
                "box-shadow":"none",
                "border-radius":"0",
                "cursor":"wait"
                //"opacity":"0.4"
            })
        }
    }

    $("#regStudyNumber").on('input',function(e){
        console.log($(this).val().length);
        stateChange()

    });
    $("#regTrueName").on('input',function(e){
        console.log($(this).val().length);
        stateChange()

    });
    $("#regSubmitPart2").click(function(){
        //alert(111)
        $(this).css({
            "background-color":"rgba(135, 255, 96, 0.8)",
            "color":"rgba(255, 255, 255, 0.98)",
            "box-shadow":"none",
            "border-radius":"0"
        })
    })
}