/**
 * Created by shaoning on 2018/4/29.
 */
$(".codeExplainInput").blur(function(){
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
});

function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg); //匹配目标参数
    if (r != null) return unescape(r[2]); return null; //返回参数值
}


function goNextDirInit(){
    $(".goToNextDir").unbind('click').click(function(){
        var clickDirORFileNameString=$(this).attr("id")
        if (clickDirORFileNameString.split("%")[0]=="thisDirName") {
            // console.log({
            //     "currentDirPath":$("#currentDirPath").text().replace(/[\r\n]/g,""),
            //     "clickDirName":clickDirORFileNameString.split("%")[1],
            //     "currentCodeSecondNumber":getUrlParam("codeManageSecondNumber")
            // })
            $.post("selfPart/codeOneVersionGetNextDir",{"currentDirPath":$("#currentDirPath").text().replace(/[\r\n]/g,""),"clickDirName":clickDirORFileNameString.split("%")[1],"currentCodeSecondNumber":getUrlParam("codeManageSecondNumber")},function(getNextDirAndFileList){
                var willAddNewDirString = ""
                $(".currentDirShow").removeClass("currentDirShow")
                $("#currentDirPath").append('<span class="currentDirPathShow currentDirShow" id="'+getNextDirAndFileList["currentAllPath"]+getNextDirAndFileList["currentDir"]+'/">'+getNextDirAndFileList["currentDir"]+'<span class="currentDirPathShowSeparator">/</span></span>')
                $.each(getNextDirAndFileList["getListDirs"],function(index,OneDir){
                    if (OneDir!="^^") {
                        willAddNewDirString += '<div class="goToNextDir" id="thisDirName%'+OneDir+'"><i class="iconfont">&#xe61d;</i>'+OneDir+' </div>'
                    };
                })
                $.each(getNextDirAndFileList["getListFiles"],function(index,OneFile){
                    if (OneFile!="^^") {
                        willAddNewDirString += '<div class="goToNextDir" id="thisFileName%'+OneFile+'"><i class="iconfont">&#xe63d;</i>'+OneFile+'</div>'
                    };
                })
                $("#goToNextDirShowWindow").empty().append(willAddNewDirString)
                goNextDirInit()
                getLastDirByAllPath()
            })
        }else{
            console.log("文件")
        };
        // $.post("selfPart/codeOneVersionGetPath",{})
    })
}
goNextDirInit()


function basename(direct) {
    if (!direct) return '';
    if (direct.indexOf('/') !== -1) {
        var result = direct.split('/');
        var a = result.pop();
        while (a ==='') {
            a = result.pop();
        }
        return a || '';
    } else {
        return direct;
    }
}

// data
// clickDirName:"app_codeManage"
// currentCodeSecondNumber:"20180505194335_c16"
// currentDirPath"codeManageAndShare/"

$(".baseDir").click(function(){
    window.location.reload()
})

function getLastDirByAllPath(){
    $(".currentDirPathShow").not(".baseDir").unbind('click').click(function(){
        $(".currentDirShow").removeClass("currentDirShow")
        $(this).addClass("currentDirShow")
        var dirPath=$(this).attr("id")
        // console.log(basename(dirPath))
        console.log(dirPath.split(basename(dirPath))[0])
        $(this).nextAll().remove()
        $.post("selfPart/codeOneVersionGetNextDir",{
            "currentDirPath":dirPath.split(basename(dirPath))[0],
            "clickDirName":basename(dirPath),
            "currentCodeSecondNumber":getUrlParam("codeManageSecondNumber")
        },function(getNextDirAndFileList){
            var willAddNewDirString = ""
            // $("#currentDirPath").append('<span class="currentDirPathShow" id="'+getNextDirAndFileList["currentAllPath"]+getNextDirAndFileList["currentDir"]+'/">'+getNextDirAndFileList["currentDir"]+'<span class="currentDirPathShowSeparator">/</span></span>')
            $.each(getNextDirAndFileList["getListDirs"],function(index,OneDir){
                if (OneDir!="^^") {
                    willAddNewDirString += '<div class="goToNextDir" id="thisDirName%'+OneDir+'"><i class="iconfont">&#xe61d;</i>'+OneDir+' </div>'
                };
            })
                $.each(getNextDirAndFileList["getListFiles"],function(index,OneFile){
                if (OneFile!="^^") {
                    willAddNewDirString += '<div class="goToNextDir" id="thisFileName%'+OneFile+'"><i class="iconfont">&#xe63d;</i>'+OneFile+'</div>'
                };
            })
            $("#goToNextDirShowWindow").empty().append(willAddNewDirString)
            goNextDirInit()
            // getLastDirByAllPath()
        })
    })
}
getLastDirByAllPath()

$(".returnLastDir").click(function(){
    $(".currentDirShow").prev().click()
})