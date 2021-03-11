/**
 * Created by shaoning on 2018/4/14.
 */
 function picUpload(){
    var form_data = new FormData();
    var file_info =$( '#selfImageChangeButton')[0].files[0];
    form_data.append('file',file_info);
    if(file_info==undefined){//暂且不许要判断是否有附件
        console.log('你没有要更换的头像图片');
        return false
    }
    $.ajax({
        url:'/selfPart/changeUserPic',
        type:'POST',
        data: form_data,
        processData: false,  // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function(callback) {
            console.log('上传成功')
            window.location.href="/selfPart"
            return true
        }
    });
}
function imgPreview(fileDom) {
    //判断是否支持FileReader
    if (window.FileReader) {
        var reader = new FileReader();
    } else {
        alert("您的设备不支持图片预览功能，如需该功能请升级您的设备！");
    }
    //获取文件
    var file = fileDom.files[0];
    var imageType = /^image\//;
    //是否是图片
    if (!imageType.test(file.type)) {
        alert("请选择图片！");
        return;
    }
    //读取完成
    reader.onload = function (e) {
        picUpload()
        //获取图片dom
        var img = document.getElementById("selfImage");
        //图片路径设置为读取的图片
        img.src = e.target.result;
        // console.log(img.src) 
    };
    reader.readAsDataURL(file);
}
$("#selfImage").click(function () {
    $("#selfImageChangeButton").click();
});
