/**
 * Created by shaoning on 2018/4/28.
 */
function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg); //匹配目标参数
    if (r != null) return unescape(r[2]); return null; //返回参数值
}
function getDynamicSelf(){
	$.post("/otherPart/getDynamic",{"userID":getUrlParam("userID")},function(allMessageUserNumbers){
		var getDynamicSelf="";
		var currentMonth="";
		var currentDate="";
		for(i in allMessageUserNumbers){
			// console.log(allMessageUserNumbers[i])
			var date = allMessageUserNumbers[i]["selfPartUserDynamicTime"].split(" ")[0];
			var thisMonth = date.split("-")[1].charAt(0)=="0" ? date.split("-")[1].charAt(1) : date.split("-")[1];
			var dynamicExplain="";
			// console.log("获取此条动态的月份："+thisMonth)
			if (currentMonth!=thisMonth) {
				 getDynamicSelf+=('<div class="date_month">'+thisMonth+'月</div>');
				 currentMonth=thisMonth
			};
			if (currentDate!=date) {
				getDynamicSelf+=('<div class="date_oneDay"><div class="leadIcon"><i class="iconfont">&#xe618;</i></div><span class="date_oneDay_show">'+date+'</span></div>');
				currentDate=date
			};
			if (allMessageUserNumbers[i]["selfPartUserDynamicType"]=="data_addDate") {
				dynamicExplain="添加新项目";
			}else if (allMessageUserNumbers[i]["selfPartUserDynamicType"]=="data_update") {
				dynamicExplain="提交新版本";
			};
			getDynamicSelf+=('<div class="'+allMessageUserNumbers[i]["selfPartUserDynamicType"]+
				'"><div class="leadIcon"><i class="iconfont">&#'+allMessageUserNumbers[i]["selfPartUserDynamicPic"]+
				';</i></div><span>'+dynamicExplain+'<a href="/selfPart/codeOneVersion?codeManageSecondNumber='+allMessageUserNumbers[i]["selfPartUserDynamicCodeSecondNumber"]+'">'+allMessageUserNumbers[i]["selfPartUserDynamicCodeName"]+
				'</a>：'+allMessageUserNumbers[i]["selfPartUserDynamicExplain"]+'</span><div class="data_update_time">'+
				allMessageUserNumbers[i]["selfPartUserDynamicTime"].split(" ")[1]+
				'</div></div>');
		}
	    getDynamicSelf+=('');
	    if (getDynamicSelf=="") {
	    	getDynamicSelf+='<div style="font-size:100px;text-align:center;color:#929292bd">ta很懒</br>什么动态</br>都没有</div>'
	    	$("#mainShowBodyControlNewInfAllContent").css({
	    		"border":"none"
	    	})
	    };
	    // console.log(getDynamicSelf)
	    $(".mainShowBodyControlNewInfAllContentSelf").append(getDynamicSelf);
	    //console.log(date.split("-")[1])
    });
}
getDynamicSelf();