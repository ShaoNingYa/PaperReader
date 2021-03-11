/**
 * Created by 邵宁 on 2018/05/08 0029.
 */
 $(".mainShowRightAll").css({"margin-top":"30px"})
$.get("/index/getHotTag",function(getPushHotTagToIndex){
	$(".mainShowRight").eq(0).find(".mainShowRightHotTag").remove()
	$.each(getPushHotTagToIndex,function(id,tagName){
		$(".mainShowRight").eq(0).append('<a href="/index?tag=codeTag_'+id+'"><span class="mainShowRightHotTag">&nbsp; '+tagName+' &nbsp;</span></a>')
		// <a href=""><span class="mainShowRightHotTag">&nbsp; aaa &nbsp;</span></a>
	})
	// 热门标签点击事件：
	$(".mainShowRightHotTag").click(function(){
		$("#moveToFlag_3").click()
		$("#codeTag_"+$(this).attr("id").split("_")[1]).click()
	})
})
$.post("/selfPart/getHotestCode",function(getResult){
	console.log(getResult)
	$(".mainShowRight").eq(1).find("a").remove()
	var getHotestCodeString=''
	$.each(getResult,function(index,oneHotestCode){
		getHotestCodeString+='<a href="/selfPart/codeOneVersion?codeManageSecondNumber='+oneHotestCode["codeSecondNumber"]+'">'
		getHotestCodeString+='<div class="mainShowRightHotInfo">'
		getHotestCodeString+='<strong>'+oneHotestCode["codeName"]+"</strong>："+oneHotestCode["codeExplain"]
		getHotestCodeString+='</div></a>'
	})
	$(".mainShowRight").eq(1).append(getHotestCodeString)
})
$.post("selfPart/getNewestDiscuss",function(getResult){
	// console.log(getResult)
	$(".mainShowRight").eq(2).find(".latestDiscuss").remove()
	var getNewestDiscussString=''
	// '<a href="">dfgzdf服务萨尔发我色法,分为非IO误会而覅公安侮辱狗皮肤爱好歌颂和偶然苹果好二个人爱好而广佛怕和你温柔过</a>'
	$.each(getResult,function(index,oneDiscuss){
		getNewestDiscussString+='<div class="latestDiscuss">'
		getNewestDiscussString+='<a href=/selfPart/codeOneVersion?codeManageSecondNumber='+oneDiscuss["codeSecondNumber"]+'>'
		getNewestDiscussString+=oneDiscuss["userName"] +"："+ oneDiscuss["discussContent"]
		getNewestDiscussString+='</a>'
		getNewestDiscussString+='</div>'
	})
	$(".mainShowRight").eq(2).append(getNewestDiscussString)
})
// $(".mainShowRight").append('<a href=""><div class="mainShowRightHotInfo">fadsfasdfasefe</div></a>')
// $(".mainShowRight").append('<a href=""><div class="mainShowRightHotInfo">fadsfasdfasefe</div></a>')