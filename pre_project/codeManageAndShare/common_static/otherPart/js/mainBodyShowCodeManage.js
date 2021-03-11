/**
 * Created by shaoning on 2018/4/11.
 */
 function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg); //匹配目标参数
    if (r != null) return unescape(r[2]); return null; //返回参数值
}
$.post("/otherPart/getCodeSimple",{"userID":getUrlParam("userID")},function(allCodeSimples){
    // console.log("allCodeSimples:"+allCodeSimples)
    var codeAllShow=""
    for(allCodeSimplesIndex in allCodeSimples){
        // console.log("allCodeSimples[allCodeSimplesIndex]")
        // console.log(allCodeSimples[allCodeSimplesIndex])
        allCodeSimpleFirsts = allCodeSimples[allCodeSimplesIndex]
        // console.log(allCodeSimpleFirsts)
        // console.log(allCodeSimplesIndex)
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePart" id="mainShowBodyShowCodeManageCodeShowOnePart_'+allCodeSimplesIndex+'">'
        var getFirstName = "";
        var getIsShare = 1;
        var getIsShareText="不公开"
        var getLanguage = "";
        var getNewTime = "";
        var getAllTags="";
        var getAllSearchTimes=0;
        var getAllCheckTimes=0;
        var getAllDownloadTimes=0;
        var getExplain="";
        for(forGetThisCodeName in allCodeSimpleFirsts){
            if (forGetThisCodeName!="codeFirstNumber") {
                getFirstName = allCodeSimpleFirsts[forGetThisCodeName]["codeName"]
                getIsShare = allCodeSimpleFirsts[forGetThisCodeName]["codeIsShare"]
                getLanguage = allCodeSimpleFirsts[forGetThisCodeName]["codeLanguage"]
                getNewTime = allCodeSimpleFirsts[forGetThisCodeName]["codeUploadTime"]
                getAllTags += allCodeSimpleFirsts[forGetThisCodeName]["codeAllTags"].join(" ")
                getAllSearchTimes += parseInt(allCodeSimpleFirsts[forGetThisCodeName]["codeSerchTimes"])
                getAllCheckTimes += parseInt(allCodeSimpleFirsts[forGetThisCodeName]["codeCheckTimes"])
                getAllDownloadTimes += parseInt(allCodeSimpleFirsts[forGetThisCodeName]["codeDownloadTimes"])
                if (getExplain=="") {getExplain = allCodeSimpleFirsts[forGetThisCodeName]["codeExplain"]};//取第一个说明
            };
        }
        if (getIsShare) {getIsShareText="公开"};
        // console.log("获取公开状态："+getIsShareText)
        // console.log("获取程序名:"+getFirstName)
        // console.log("获取程序语言:"+getLanguage)
        // console.log("获取程序最新修改时间:"+getNewTime)
        // console.log("获取程序的所有标签："+getAllTags)
        // console.log("获取程序的所有索引次数："+getAllSearchTimes)
        // console.log("获取程序的所有下载次数："+getAllDownloadTimes)
        // console.log("获取程序的所有查看次数："+getAllCheckTimes)
        // console.log("获取程序的说明："+getExplain)
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartTitle"><a href="/selfPart/codeOneProject?codeManageFirstNumber='+allCodeSimpleFirsts["codeFirstNumber"]+'">'+getFirstName+'</a><span class="mainShowBodyShowCodeManageCodeShowOnePartTitleIsPublic">分享状态：'+getIsShareText+'</span></div>'
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartLanguage">使用的语言：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getLanguage+'</span></div>'
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartLastTime">最新一次修改时间：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getNewTime+'</span></div>'
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartLabel">所属标签：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getAllTags+'</span></div><br/>'
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartSearchTimes">总索引次数：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getAllSearchTimes+'</span></div>'
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartCheckTimes">总查看次数：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getAllCheckTimes+'</span></div>'
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartDownloadTimes">总下载次数：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush">'+getAllDownloadTimes+'</span></div><br/>'
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartResume_hide">简要描述：<span class="mainShowBodyShowCodeManageCodeShowOnePartPush" title="'+getExplain+'">'+getExplain+'</span></div>'
        codeAllShow+='<div class="mainShowBodyShowCodeManageCodeShowOnePartByTime">'
        codeAllShow+='<table class="mainShowBodyShowCodeManageCodeShowOnePartByTimeBodyShow">'
        codeAllShow+='<tr><th style="width: 25%;!important;">提交时间</th><th style="width: 75%;!important;">更改说明</th></tr>'
        //<th style="width: 15%;!important;">更改版本号</th>
        var getAllCodeForSeconds=[]
        for(allCodeSimpleFirstAll in allCodeSimpleFirsts){//这里是每个单独的小版本
            if (allCodeSimpleFirstAll!="codeFirstNumber") {
                // console.log(allCodeSimpleFirstAll)
                //<td><a href="">'+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeSecondNumber"]+'</a></td>
                getAllCodeForSeconds.unshift('<tr><td>'+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeUploadTime"]+'</td><td class="mainShowBodyShowCodeManageCodeShowOnePartByTimeBodyShowTd" title="'+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeExplain"]+'"><a href="/selfPart/codeOneVersion?codeManageSecondNumber='+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeSecondNumber"]+'">'+allCodeSimpleFirsts[allCodeSimpleFirstAll]["codeExplain"]+'</a></td></tr>')
            }
        }
        for(getAllCodeForSecondIndex in getAllCodeForSeconds){
            codeAllShow+=getAllCodeForSeconds[getAllCodeForSecondIndex]
        }
        codeAllShow+='</table></div></div>'
    }
    if (codeAllShow=="") {
        codeAllShow+='<div style="font-size:100px;text-align:center;color:#929292bd">ta很懒</br>什么都</br>没有留下</div>'
    };
    $("#mainShowBodyShowCodeManage").append(codeAllShow)
    mainShowBodyShowCodeManageCodeShowOnePartInit()
    // console.log(codeAllShow)
});
function mainShowBodyShowCodeManageCodeShowOnePartInit(){
    var mainShowBodyShowCodeManageCodeShowOnePart=$(".mainShowBodyShowCodeManageCodeShowOnePart");
    mainShowBodyShowCodeManageCodeShowOnePart.alt=0;
    mainShowBodyShowCodeManageCodeShowOnePart.click(function(){
        event.stopPropagation();
        if(this.alt==undefined){
            //console.log(undefined);
            this.alt=0;
        }
        //console.log(this.alt);
        if(this.alt==0){
            $(this).css({
                "height":"500px"
            });
            //$($(this).children('div')[$(this).children('div').length-2]).removeClass("mainShowBodyShowCodeManageCodeShowOnePartResume_hide").addClass("mainShowBodyShowCodeManageCodeShowOnePartResume_show");
            $($(this).children('.mainShowBodyShowCodeManageCodeShowOnePartByTime')).stop().slideDown(500);
            this.alt=1;
            //console.log(this.id);
        }else{
            $(this).css({
                "height":"150px"
            });
            //$($(this).children('div')[$(this).children('div').length-2]).removeClass("mainShowBodyShowCodeManageCodeShowOnePartResume_show").addClass("mainShowBodyShowCodeManageCodeShowOnePartResume_hide");
            $($(this).children('.mainShowBodyShowCodeManageCodeShowOnePartByTime')).stop().slideUp(250);
            this.alt=0;
        }
    });
    $("html").click(function(){
        var mainShowBodyShowCodeManageCodeShowOnePart=$(".mainShowBodyShowCodeManageCodeShowOnePart");
        mainShowBodyShowCodeManageCodeShowOnePart.css({
            "height":"150px"
        });
        $("#mainShowBodyShowCodeManageCodeShowOnePartAddNewProject").css({
            "height":"100px"
        });
        $('.mainShowBodyShowCodeManageCodeShowOnePartByTime').stop().slideUp(250);
        for(var i=0;i<mainShowBodyShowCodeManageCodeShowOnePart.length;i++){
            mainShowBodyShowCodeManageCodeShowOnePart[i].alt=0;
        }
    });
}
mainShowBodyShowCodeManageCodeShowOnePartInit()