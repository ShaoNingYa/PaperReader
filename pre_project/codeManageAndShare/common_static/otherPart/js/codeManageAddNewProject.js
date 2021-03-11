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
}).keydown(function () {
    if (event.keyCode == 13) {
        //alert("提交")
        //console.log("回车");
        //console.log("回车"+this.id);
        $("#send_"+this.id.split("_")[1]).click();
    }
});

//下面这个函数功能是获取所有选择的标签，将其组合成字符串
function getBeChoiceTag(){
    var allBeChoiceTagList = []
    var getAllBeChoiceTagByClassObject = $(".codeTagOneClass")
    for(var i=0;i<getAllBeChoiceTagByClassObject.length;i++){
        // getAllBeChoiceTagByClassObject[i].alt=0;
        // console.log(getAllBeChoiceTagByClassObject[i].alt)
        if(getAllBeChoiceTagByClassObject[i].alt==1 && getAllBeChoiceTagByClassObject[i].id!="addNewCodeTag"){
            console.log(getAllBeChoiceTagByClassObject[i].id)
            allBeChoiceTagList.push(getAllBeChoiceTagByClassObject[i].id.split("_")[1])
        }
    }
    return allBeChoiceTagList.join(",")
}


function codeUpload(){
    var form_data = new FormData();
    var file_info =$( '#openCodeSrc')[0].files[0];
    form_data.append('file',file_info);
    var codeProjectName = $("#codeProjectName").val()
    var languageChoice = $("#languageChoice").val().split("_")[1]
    var isShare = $("#isShare").val()
    var codeExplain = $("#codeExplain").text()
    var codeTag = getBeChoiceTag()
    form_data.append('codeProjectName',codeProjectName);
    form_data.append('languageChoice',languageChoice);
    form_data.append('isShare',isShare);
    form_data.append('codeExplain',codeExplain);
    form_data.append('codeTag',codeTag);
    if(file_info==undefined){//暂且不许要判断是否有附件
        alert('你没有选择任何文件');
        return false
    }
    $.ajax({
        url:'/selfPart/codeManageUploadAjax',
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

//下面是添加标签被点击事件
$(".codeTagOneClassAddTag").click(function(){
        // console.log(this.alt)
        if (this.alt != 1) {
            $(this).addClass("codeTagOneClassBeChoiceAddTag")
            this.alt = 1
        }else{
            $(this).removeClass("codeTagOneClassBeChoiceAddTag")
            this.alt = 0
        };
    })
// 下面是标签点击事件
// function codeTagInit(){
    $(".codeTagOneClass").click(function(){
        event.stopPropagation();
        // console.log(this.alt)
        if (this.alt != 1) {
            if (getBeChoiceTag().split(",").length<4) {
                $(this).addClass("codeTagOneClassBeChoice")
                this.alt = 1
            }else{
                alert("已选标签个数达到上限")
            }; 
        }else{
            $(this).removeClass("codeTagOneClassBeChoice")
            this.alt = 0
        };
    })
// }
// codeTagInit()

//下面是创建标签
$("#addNewCodeTag").click(function(){
     event.stopPropagation();
    $("#addANewCodeTag").toggle(1000)
    $("#addANewCodeTagName").focus()
    if ($(this).attr("alt")==1) {
        $(this).attr("alt","0")
    }else{
        $(this).attr("alt","1")
    };
});
$("#addANewCodeTagName").click(function(){
    event.stopPropagation();
})
$("html").click(function(){
    // console.log($("#addNewCodeTag").attr("alt"))
    if ($("#addNewCodeTag").attr("alt")==1) {
        $("#addNewCodeTag").click()
    };
})
$("#addANewCodeTagSubmit").click(function(){
    event.stopPropagation();
    // console.log($("#addANewCodeTagName").val())
    getNewTagName = $("#addANewCodeTagName").val()
    if (getNewTagName=="") {
        alert("标签名不可为空")
        $("#addANewCodeTagName").focus()
        return false
    };
    $.post("/selfPart/addOneCodeTag",{"codeTagName":getNewTagName},function(getThisTagId){
        var getNewTag = '<div class="codeTagOneClass" id="codeTag_'+getThisTagId+'" style="background-color:#ff00006e;">'+getNewTagName+'</div>'
        $("#addNewCodeTag").after(getNewTag)
        $("#codeTag_"+getThisTagId).click(function(){
            event.stopPropagation();
            // console.log(this.alt)
            if (this.alt != 1) {
                if (getBeChoiceTag().split(",").length<4) {
                    $(this).addClass("codeTagOneClassBeChoice")
                    this.alt = 1
                }else{
                    alert("已选标签个数达到上限")
                }; 
            }else{
                $(this).removeClass("codeTagOneClassBeChoice")
                this.alt = 0
            };
        })//.click()
        $("#addANewCodeTagName").val("")
        $("#addNewCodeTag").click()
    });
})
 