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


function GetQueryString(name)
{
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);
     if(r!=null)return  unescape(r[2]); return null;
}

function codeUpload(){
    var form_data = new FormData();
    var file_info =$( '#openCodeSrc')[0].files[0];
    form_data.append('file',file_info);
    var codeProjectName = $("#codeProjectName").val()
    var codeFirstNumber = GetQueryString("codeManageFirstNumber")
    var languageChoice = $("#languageChoice").val().split("_")[1]
    var isShare = $("#isShare").val()
    var codeExplain = $("#codeExplain").text()
    // var codeTag = getBeChoiceTag()
    form_data.append('codeFirstNumber',codeFirstNumber);
    form_data.append('codeProjectName',codeProjectName);
    form_data.append('languageChoice',languageChoice);
    form_data.append('isShare',isShare);
    form_data.append('codeExplain',codeExplain);
    // form_data.append('codeTag',codeTag);
    if(file_info==undefined){//暂且不许要判断是否有附件
        alert('你没有选择任何文件');
        return false
    }
    $.ajax({
        url:'/selfPart/codeManageUploadAjaxNewVersion',
        type:'POST',
        data: form_data,
        processData: false,  // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function(callback) {
            console.log('ok')
            window.location.href="/selfPart"
        }
    });
}

$("#addProjectSubmit").click(function(){
    codeUpload();
})
