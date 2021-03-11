/**
 * Created by shaoning on 2018/4/29.
 */
function checkFileDetilInit(){
    $(".changeFile").unbind().click(function(e){
        event.stopPropagation();
        if (e.ctrlKey==false) {
            var codeFileInfo = {}
            codeFileInfo["codeAllPath"] = $(this).attr("id").split(">")[1]
            $.post("selfPart/codeOneFileShowForProject",codeFileInfo,function(getCodeFileCode){
                if (getCodeFileCode["file"]) {
                    window.location.href=getCodeFileCode["file"]
                }else{
                    $(".getCodeFileCodeShowDivAll").remove()
                    $("html").css({"overflow-y":"hidden"})
                    $("body").append('<div id="getCodeFileCodeShowDiv" class="getCodeFileCodeShowDivAll">'+getCodeFileCode+'</div>')
                }
            })
        }else{
            var getCodeDifferentFileLast = $(this).attr("id").split(">")[0]
            var getCodeDifferentFileThis = $(this).attr("id").split(">")[1]
            $.post("selfPart/getCodeCompare_ChangeDetil",{"getCodeDifferentFileLast":getCodeDifferentFileLast,"getCodeDifferentFileThis":getCodeDifferentFileThis},function(getDifferentHTML){
                $("html").css({"overflow-y":"hidden"})
                $("body").append('<div id="getDifferentHTMLShowDiv" class="scrollForDifferentShow">'+getDifferentHTML+'</div>')
                $("#getDifferentHTMLShowDiv").click(function(){
                    $(this).remove()
                    $("html").css({"overflow-y":"scroll"})
                })
            })
        }
        
    })
    $(".addFile").unbind().click(function(e){
        event.stopPropagation();
        if (e.ctrlKey==false){
            var codeFileInfo = {}
            codeFileInfo["codeAllPath"] = $(this).attr("id")
            $.post("selfPart/codeOneFileShowForProject",codeFileInfo,function(getCodeFileCode){
                if (getCodeFileCode["file"]) {
                    window.location.href=getCodeFileCode["file"]
                }else{
                    $(".getCodeFileCodeShowDivAll").remove()
                    $("html").css({"overflow-y":"hidden"})
                    $("body").append('<div id="getCodeFileCodeShowDiv" class="getCodeFileCodeShowDivAll">'+getCodeFileCode+'</div>')
                }
            })
        }else{
            window.location.href="/"+$(this).attr("id").split("common_")[1]
        }
    })
    $(".delFile").unbind().click(function(e){
        event.stopPropagation();
        if (e.ctrlKey==false){
            var codeFileInfo = {}
            codeFileInfo["codeAllPath"] = $(this).attr("id")
            $.post("selfPart/codeOneFileShowForProject",codeFileInfo,function(getCodeFileCode){
                if (getCodeFileCode["file"]) {
                    window.location.href=getCodeFileCode["file"]
                }else{
                    $(".getCodeFileCodeShowDivAll").remove()
                    $("html").css({"overflow-y":"hidden"})
                    $("body").append('<div id="getCodeFileCodeShowDiv" class="getCodeFileCodeShowDivAll">'+getCodeFileCode+'</div>')
                }
            })
        }else{
            window.location.href="/"+$(this).attr("id").split("common_")[1]
        }
    })
}

$(".OneVersion").click(function(){
    var thisSecondNumber = $(this).find(".OneVersionTitle1").text()
    var lastSecondNumber = ""
    // console.log($(".OneVersion").index(this))
    thisIndexNumber = $(".OneVersion").index(this)
    if (thisIndexNumber!=0) {
        // console.log($(".OneVersion").eq(thisIndexNumber-1).find(".OneVersionTitle1").text())
        lastSecondNumber = $(".OneVersion").eq(thisIndexNumber-1).find(".OneVersionTitle1").text()
    };
    // console.log("thisSecondNumber:"+thisSecondNumber)
    // console.log("lastSecondNumber:"+lastSecondNumber)
    var getCodeChangeDetil = $(this).find(".codeChangeDetil")
    getCodeChangeDetil.slideToggle("slow")
    if ($(this).attr("alt")!=1) {
        $(this).attr("alt","1")
        $.post("/selfPart/getCodeCompare?CodeManageSecondNumber",{"thisSecondNumber":thisSecondNumber,"lastSecondNumber":lastSecondNumber},function(allCodeCompareString){
            // return false
            getCodeChangeDetil.find(".codeChangeDetilShow").empty()
            allCodeCompares = allCodeCompareString.replace(/[\r\n]/g,"").split("$")
            var infoType = ""
            var infoFile = ""
            var infoTypeString = ""
            var thisInfo = ""
            for(allCodeCompareIndex in allCodeCompares){
                // console.log(allCodeCompares[allCodeCompareIndex])
                infoType = allCodeCompares[allCodeCompareIndex].split(":")[0]
                infoFile = allCodeCompares[allCodeCompareIndex].split(":")[1]
                if (infoFile!=null) {
                    // infoFile = infoFile.toString().substring(72)//.replace("common_static/codeSavePosition/","")
                    if (infoType=="addFile") {
                        infoTypeString = "添加文件"
                        thisInfo = '<div class="filePathStyle addFile" id="'+infoFile+'">'+infoTypeString+'>>>'+infoFile.substring(72) + '</div>'
                    }else if (infoType=="addDir") {
                        infoTypeString = "添加目录"
                        thisInfo = '<div class="filePathStyle addDir">'+infoTypeString+'>>>'+infoFile.substring(72) + '</div>'
                    }else if (infoType=="delDir") {
                        infoTypeString = "删除目录"
                        thisInfo = '<div class="filePathStyle delDir">'+infoTypeString+'>>>'+infoFile.substring(72) + '</div>'
                    }else if (infoType=="delFile") {
                        infoTypeString = "删除文件"
                        thisInfo = '<div class="filePathStyle delFile" id="'+infoFile+'">'+infoTypeString+'>>>'+infoFile.substring(72) + '</div>'
                    }else if (infoType=="changeFile") {
                        infoTypeString = "修改文件"
                        thisInfo = '<div class="filePathStyle changeFile" id="'+infoFile+'">'+infoTypeString+'>>>'+infoFile.split(">")[1].substring(72) + '</div>'
                    };                
                    // thisInfo = '<div>'+infoTypeString+'>>>'+infoFile + '</div>'
                    getCodeChangeDetil.find(".codeChangeDetilShow").append(thisInfo)
                };
                // 
            }
            checkFileDetilInit()
            // getCodeChangeDetil.find(".codeChangeDetilShow").append(allCodeCompareString)
        })
    };
})
$(".codeDownload").click(function(){
    event.stopPropagation();
})
$(".OneVersionTitle1").click(function(){
    event.stopPropagation();
})
document.onkeydown=function(event){
    var e = event || window.event || arguments.callee.caller.arguments[0];
    if(e && e.keyCode==8){ // 按 回退
        $(".returnLastDir").click()
    }else if(e && e.keyCode==27){ // 按 Esc
        $("#getCodeFileCodeShowDiv").remove()
        $(".getCodeFileCodeShowDivAll").remove()
        $("html").css({"overflow-y":"auto"})
    }
};

// $.post("/selfPart/getCodeCompare",function(allCodeSimples){
//     // console.log("allCodeSimples:"+allCodeSimples)
//     var codeAllShow=""
//     for(allCodeSimplesIndex in allCodeSimples){
//         // console.log("allCodeSimples[allCodeSimplesIndex]")
//         // console.log(allCodeSimples[allCodeSimplesIndex])
//         allCodeSimpleFirsts = allCodeSimples[allCodeSimplesIndex]
//         // console.log(allCodeSimpleFirsts)
//         // console.log(allCodeSimplesIndex)
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePart" id="mainShowBodyShowCodeManageCodeShowOnePart_'+allCodeSimplesIndex+'">'
//         var getFirstName = "";
//         var getIsShare = 1;
//         var getIsShareText="不公开"
//         var getLanguage = "";
//         var getNewTime = "";
//         var getAllTags="";
//         var getAllSearchTimes=0;
//         var getAllCheckTimes=0;
//         var getAllDownloadTimes=0;
//         var getExplain="";
//         for(forGetThisCodeName in allCodeSimpleFirsts){
//             if (forGetThisCodeName!="codeFirstNumber") {
//                 getFirstName = allCodeSimpleFirsts[forGetThisCodeName]["codeName"]
//                 getIsShare = allCodeSimpleFirsts[forGetThisCodeName]["codeIsShare"]
//                 getLanguage = allCodeSimpleFirsts[forGetThisCodeName]["codeLanguage"]
//                 getNewTime = allCodeSimpleFirsts[forGetThisCodeName]["codeUploadTime"]
//                 getAllTags += allCodeSimpleFirsts[forGetThisCodeName]["codeAllTags"].join(" ")
//                 getAllSearchTimes += parseInt(allCodeSimpleFirsts[forGetThisCodeName]["codeSerchTimes"])
//                 getAllCheckTimes += parseInt(allCodeSimpleFirsts[forGetThisCodeName]["codeCheckTimes"])
//                 getAllDownloadTimes += parseInt(allCodeSimpleFirsts[forGetThisCodeName]["codeDownloadTimes"])
//                 if (getExplain=="") {getExplain = allCodeSimpleFirsts[forGetThisCodeName]["codeExplain"]};//取第一个说明
//             };
//         }
//         if (getIsShare) {getIsShareText="公开"};
//         // console.log("获取公开状态："+getIsShareText)
//         // console.log("获取程序名:"+getFirstName)
//         // console.log("获取程序语言:"+getLanguage)
//         // console.log("获取程序最新修改时间:"+getNewTime)
//         // console.log("获取程序的所有标签："+getAllTags)
//         // console.log("获取程序的所有索引次数："+getAllSearchTimes)
//         // console.log("获取程序的所有下载次数："+getAllDownloadTimes)
//         // console.log("获取程序的所有查看次数："+getAllCheckTimes)
//         // console.log("获取程序的说明："+getExplain)
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartTitle"><a href="">'+getFirstName+'</a><span class="mainShowBodyShowCodeManageCodeShowOnePartTitleIsPublic">分享状态：'+getIsShareText+'</span></div>'
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartLanguage">使用的语言：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getLanguage+'</span></div>'
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartLastTime">最新一次修改时间：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getNewTime+'</span></div>'
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartLabel">所属标签：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getAllTags+'</span></div><br/>'
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartSearchTimes">总索引次数：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getAllSearchTimes+'</span></div>'
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartCheckTimes">总查看次数：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getAllCheckTimes+'</span></div>'
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartDownloadTimes">总下载次数：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getAllDownloadTimes+'</span></div><br/>'
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartResume_hide">简要描述：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush" title="'+getExplain+'">'+getExplain+'</span></div>'
//         codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartByTime">'
//         codeAllShow+='<table class="mainShowBodyShowCodeManageCodeShowOnePartByTimeBodyShow">'
//         codeAllShow+='<tr><th style="width: 25%;!important;">提交时间</th><th style="width: 75%;!important;">更改说明</th></tr>'
//         //<th style="width: 15%;!important;">更改版本号</th>
//         var getAllCodeForSeconds=[]
//         for(allCodeSimpleFirstAll in allCodeSimpleFirsts){//这里是每个单独的小版本
//             if (allCodeSimpleFirstAll!="codeFirstNumber") {
//                 // console.log(allCodeSimpleFirstAll)
//                 //<td><a href="">'+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeSecondNumber"]+'</a></td>
//                 getAllCodeForSeconds.unshift('<tr><td>'+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeUploadTime"]+'</td><td class="mainShowBodyShowCodeManageCodeShowOnePartByTimeBodyShowTd" title="'+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeExplain"]+'"><a href="/selfPart/codeOneVersion?codeManageSecondNumber='+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeSecondNumber"]+'">'+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeExplain"]+'</a></td></tr>')
//             }
//         }
//         for(getAllCodeForSecondIndex in getAllCodeForSeconds){
//             codeAllShow+=getAllCodeForSeconds[getAllCodeForSecondIndex]
//         }
//         codeAllShow+='</table></div></div>'
//     }
//     // console.log(codeAllShow)
//     $("#mainShowBodyShowProject").append(codeAllShow)
//     // mainShowBodyShowCodeManageCodeShowOnePartInit()
//     // console.log(codeAllShow)
// });
// function mainShowBodyShowCodeManageCodeShowOnePartInit(){
//     var mainShowBodyShowCodeManageCodeShowOnePart=$(".mainShowBodyShowCodeManageCodeShowOnePart");
//     mainShowBodyShowCodeManageCodeShowOnePart.alt=0;
//     mainShowBodyShowCodeManageCodeShowOnePart.click(function(){
//         event.stopPropagation();
//         if(this.alt==undefined){
//             //console.log(undefined);
//             this.alt=0;
//         }
//         //console.log(this.alt);
//         if(this.alt==0){
//             // $(this).css({
//             //     "height":"500px"
//             // });
//             //$($(this).children('div')[$(this).children('div').length-2]).removeClass("mainShowBodyShowCodeManageCodeShowOnePartResume_hide").addClass("mainShowBodyShowCodeManageCodeShowOnePartResume_show");
//             $($(this).children('.mainShowBodyShowCodeManageCodeShowOnePartByTime')).stop().slideDown(500);
//             this.alt=1;
//             //console.log(this.id);
//         }else{
//             // $(this).css({
//             //     "height":"150px"
//             // });
//             //$($(this).children('div')[$(this).children('div').length-2]).removeClass("mainShowBodyShowCodeManageCodeShowOnePartResume_show").addClass("mainShowBodyShowCodeManageCodeShowOnePartResume_hide");
//             $($(this).children('.mainShowBodyShowCodeManageCodeShowOnePartByTime')).stop().slideUp(250);
//             this.alt=0;
//         }
//     });
//     $("html").click(function(){
//         var mainShowBodyShowCodeManageCodeShowOnePart=$(".mainShowBodyShowCodeManageCodeShowOnePart");
//         // mainShowBodyShowCodeManageCodeShowOnePart.css({
//         //     "height":"150px"
//         // });
//         // $("#mainShowBodyShowCodeManageCodeShowOnePartAddNewProject").css({
//         //     "height":"100px"
//         // });
//         $('.mainShowBodyShowCodeManageCodeShowOnePartByTime').stop().slideUp(250);
//         for(var i=0;i<mainShowBodyShowCodeManageCodeShowOnePart.length;i++){
//             mainShowBodyShowCodeManageCodeShowOnePart[i].alt=0;
//         }
//     });
// }
// mainShowBodyShowCodeManageCodeShowOnePartInit()