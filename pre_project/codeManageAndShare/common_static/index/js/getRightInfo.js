/**
 * Created by 邵宁 on 2018/05/08 0029.
 */
$.get("/index/getHotTag",function(getPushHotTagToIndex){
	console.log(getPushHotTagToIndex)
	$.each(getPushHotTagToIndex,function(id,tagName){
		$(".mainShowRight").append('<span class="mainShowRightHotTag" id="mainShowRightHotTag_'+id+'">&nbsp; '+tagName+' &nbsp;</span>')
	})
	// 热门标签点击事件：
	$(".mainShowRightHotTag").click(function(){
		$("#moveToFlag_3").click()
		$("#codeTag_"+$(this).attr("id").split("_")[1]).click()
	})
})
$.post("/selfPart/getHotestCode",function(getResult){
	// console.log(getResult)
	// $(".mainShowRight").eq(1).find("a").remove()
	var getHotestCodeString=''
	$.each(getResult,function(index,oneHotestCode){
		getHotestCodeString+='<a href="/selfPart/codeOneVersion?codeManageSecondNumber='+oneHotestCode["codeSecondNumber"]+'">'
		getHotestCodeString+='<div class="mainShowRightHotInfo">'
		getHotestCodeString+='<strong>'+oneHotestCode["codeName"]+"</strong>："+oneHotestCode["codeExplain"]
		getHotestCodeString+='</div></a>'
	})
	$(".mainShowRight").append(getHotestCodeString)
	$(".mainShowRightHotInfo").eq(0).css({
		"height":"80px",
		"line-height":"80px",
		"font-size":"32px",
		"color":"#ff5d5d"
	}).prepend("第一名：")
	$(".mainShowRightHotInfo").eq(1).css({
		"height":"70px",
		"line-height":"70px",
		"font-size":"27px",
		"color":"#ff7400e8"
	}).prepend("第二名：")
	$(".mainShowRightHotInfo").eq(2).css({
		"height":"60px",
		"line-height":"60px",
		"font-size":"22px",
		"color":"#9b9601"
	}).prepend("第三名：")
})
// $(".mainShowRight").append('<a href=""><div class="mainShowRightHotInfo">fadsfasdfasefe</div></a>')
// $(".mainShowRight").append('<a href=""><div class="mainShowRightHotInfo">fadsfasdfasefe</div></a>')