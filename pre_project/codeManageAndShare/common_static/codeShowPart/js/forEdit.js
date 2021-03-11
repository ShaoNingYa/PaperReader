/**
 * Created by shaoning on 2018/2/1.
 */
    //初始化对象
editor = ace.edit("code");
//设置风格和语言（更多风格和语言，请到github上相应目录查看）
theme = "clouds";
language = "html";
editor.setTheme("ace/theme/" + theme);
editor.session.setMode("ace/mode/" + language);
//字体大小
editor.setFontSize(18);
//设置只读（true时只读，用于展示代码）
editor.setReadOnly(true);
//自动换行,设置为off关闭
editor.setOption("wrap", "free");
editor.blur()

//启用提示菜单
ace.require("language_tools");
editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true
});
//editor.setValue(editor.getValue());
// editor.setValue("zheshiceshi");
editor.session.setMode("ace/mode/" + $(".definedCodeType").attr("id"));
// document.onkeydown=function(event){
//     var e = event || window.event || arguments.callee.caller.arguments[0];
//     if(e && e.keyCode==27){ // 按 Esc
//         //$("#codeFullScreen").css("display","none");
//         //$("body").css("overflow-y","auto");
//     }
//     //if(e && e.keyCode==113){ // 按 F2
//     //    //要做的事情
//     //}
//     //if(e && e.keyCode==13){ // enter 键
//     //    //要做的事情
//     //}
// };