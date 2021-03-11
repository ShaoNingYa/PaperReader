/**
 * Created by shaoning on 2018/4/28.
 */

function getDynamicAll(){
    $.post("/selfPart/getDynamicForAllFocus",function(allMessageUserNumbers){
		var getDynamicSelf="";
		var currentMonth="";
		var currentDate="";
		var currentUserName="";
		var deleteVersionSecondList=[]
		for(i in allMessageUserNumbers){
			// console.log(allMessageUserNumbers[i])
			var date = allMessageUserNumbers[i]["selfPartUserDynamicTime"].split(" ")[0];
			var thisMonth = date.split("-")[1].charAt(0)=="0" ? date.split("-")[1].charAt(1) : date.split("-")[1];
			var thisUserName = allMessageUserNumbers[i]["selfPartUserName"]
			var thisUserID = allMessageUserNumbers[i]["selfPartUserID"]
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
			if (currentUserName!=thisUserName) {
				getDynamicSelf+=('<div class="user"><img src="'+allMessageUserNumbers[i]["selfPartUserPic"]+'" alt="" class="userPic lead"/><a href="/otherPart/?userID='+thisUserID+'"><span class="userName">'+thisUserName+'</span></a></div>');
				currentUserName=thisUserName
			};
			if (allMessageUserNumbers[i]["selfPartUserDynamicType"]=="data_addDate") {
				dynamicExplain="添加新项目";
			}else if (allMessageUserNumbers[i]["selfPartUserDynamicType"]=="data_update") {
				dynamicExplain="提交新版本";
			}else if (allMessageUserNumbers[i]["selfPartUserDynamicType"]=="data_delDate") {
				dynamicExplain="删除老版本";
				deleteVersionSecondList.push(allMessageUserNumbers[i]["selfPartUserDynamicCodeSecondNumber"])
			};
			getDynamicSelf+=('<div class="'+allMessageUserNumbers[i]["selfPartUserDynamicType"]+
				'"><div class="leadIcon"><i class="iconfont">&#'+allMessageUserNumbers[i]["selfPartUserDynamicPic"]+
				';</i></div><span>'+dynamicExplain+'<a href="/selfPart/codeOneVersion?codeManageSecondNumber='+allMessageUserNumbers[i]["selfPartUserDynamicCodeSecondNumber"]+'">'+allMessageUserNumbers[i]["selfPartUserDynamicCodeName"]+
				'</a>：'+allMessageUserNumbers[i]["selfPartUserDynamicExplain"]+'</span><div class="data_update_time">'+
				allMessageUserNumbers[i]["selfPartUserDynamicTime"].split(" ")[1]+
				'</div></div>');
		}
	    getDynamicSelf+=('');
	    getDynamicSelf+='<div style="width:100%;height:100px;"></div>'
	    // console.log(getDynamicSelf)
	    $(".mainShowBodyControlNewInfAllContentAll").append(getDynamicSelf);
	    //console.log(date.split("-")[1])
	    // console.log(deleteVersionSecondList)
	    $.each(deleteVersionSecondList,function(index,deleteVersionSecond){
	    	console.log(deleteVersionSecond)
	    	$("[href$="+deleteVersionSecond+"]").css({
			    "color":"#8984848a"
			})
	    })
	    
    });
}
getDynamicAll();
function getDynamicSelf(){
	$.post("/selfPart/getDynamicForMySelf",function(allMessageUserNumbers){
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
			}else if (allMessageUserNumbers[i]["selfPartUserDynamicType"]=="data_delDate") {
				dynamicExplain="删除老版本";
			};
			getDynamicSelf+=('<div class="'+allMessageUserNumbers[i]["selfPartUserDynamicType"]+
				'"><div class="leadIcon"><i class="iconfont">&#'+allMessageUserNumbers[i]["selfPartUserDynamicPic"]+
				';</i></div><span>'+dynamicExplain+'<a href="/selfPart/codeOneVersion?codeManageSecondNumber='+allMessageUserNumbers[i]["selfPartUserDynamicCodeSecondNumber"]+'">'+allMessageUserNumbers[i]["selfPartUserDynamicCodeName"]+
				'</a>：'+allMessageUserNumbers[i]["selfPartUserDynamicExplain"]+'</span><div class="data_update_time">'+
				allMessageUserNumbers[i]["selfPartUserDynamicTime"].split(" ")[1]+
				'</div></div>');
		}
	    getDynamicSelf+=('');
	    getDynamicSelf+='<div style="width:100%;height:100px;"></div>'
	    // console.log(getDynamicSelf)
	    $(".mainShowBodyControlNewInfAllContentSelf").append(getDynamicSelf);
	    //console.log(date.split("-")[1])
    });
}
getDynamicSelf();