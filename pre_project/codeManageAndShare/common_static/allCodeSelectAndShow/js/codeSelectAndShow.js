/**
 * Created by shaoning on 2018/5/6.
 */
 function getCodeInfo(){
 	$("#mainBodyCodeShow").empty().append('<img src="/static/selfPart/imgsrc/loading1.gif" style="width:100%;border:solid 3px white;opacity:0.2">')
 	var codeLanguageChoiceIs = $(".codeLanguageChoiceIs").attr("id").split("_")
 	var codeTagChoiceIs = $(".codeTagChoiceIs").attr("id").split("_")
 	var pushSelectOption={"language":codeLanguageChoiceIs[1],"codeTag":codeTagChoiceIs[1]}
 	// console.log(pushSelectOption)
 	$.post("allUser/allPartCodeSelectAndShowAjaxGetCode",pushSelectOption,function(getCodeInfo){
 		var mainBodyCodeShowString = ''
 		for(getCodeInfoIndex in getCodeInfo){
 			// console.log(getCodeInfo[getCodeInfoIndex])
 			mainBodyCodeShowString += 
	 			'<div class="OneCodeShow">'+
	                '<div class="OneCodeShowName"><a href="/selfPart/codeOneProject?codeManageFirstNumber='+getCodeInfo[getCodeInfoIndex]["codeFirstNumber"]+'">'+getCodeInfo[getCodeInfoIndex]["codeName"]+'</a></div>'+
	                '<div class="OneCodeShowAuthor">作者：<a href="/otherPart/?userID='+getCodeInfo[getCodeInfoIndex]["codeAuthorID"]+'">'+getCodeInfo[getCodeInfoIndex]["codeAuthorName"]+'</a></div>'+
	                '<div class="OneCodeShowLanguage">语言：'+getCodeInfo[getCodeInfoIndex]["codeLanguage"]+'</div>'+
	                '<div class="OneCodeShowExplain">'+getCodeInfo[getCodeInfoIndex]["codeExplain"]+'</div>'+
	                '<div class="OneCodeShowTag">'+
	                    '<div class="OneCodeShowTagTitle">所属标签:</div>'
	        $.each(getCodeInfo[getCodeInfoIndex]["codeTags"],function(codeTagID,codeTagName){
	        	mainBodyCodeShowString += '<div class="OneCodeShowTagOneTag" id="OneCodeShowTagOneTag_'+codeTagID+'">'+codeTagName+'</div>'
	        })
	        mainBodyCodeShowString += '</div></div>'
 		}
 		// mainBodyCodeShowString += '<div style="width:100%;height:100px;background-color:red"></div>'
 		$("#mainBodyCodeShow").empty().append(mainBodyCodeShowString)
 		$(".OneCodeShowTagOneTag").click(function(){
			// console.log($(this).attr("id").split("_")[1])
		   $("#codeTag_"+$(this).attr("id").split("_")[1]).click()
		});
 	})
 }
$(".codeLanguageChoice").click(function(){
    $(".codeLanguageChoiceIs").removeClass("codeLanguageChoiceIs");
    $(this).addClass("codeLanguageChoiceIs")
    getCodeInfo()
});
$(".codeTagChoice").click(function(){
    $(".codeTagChoiceIs").removeClass("codeTagChoiceIs");
    $(this).addClass("codeTagChoiceIs")
    getCodeInfo()
});
// $(".OneCodeShowTagOneTag").click(function(){
//    $("#codeTag_"+$(this).attr("id").split("_")[1]).click()
// });
$("#language_0").addClass("codeLanguageChoiceIs");
$("#codeTag_0").addClass("codeTagChoiceIs");
getCodeInfo()