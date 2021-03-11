function showCopyMessage(message, type) {
    let messageJQ = $("<div class='oneMessage'>" + message + "</div>");
    if (type == 0) {
        messageJQ.addClass("oneMessage_pre");
    } else if (type == 1) {
        messageJQ.addClass("oneMessage_trans");
    }
    /**先将原始隐藏，然后添加到页面，最后以600秒的速度下拉显示出来*/
    messageJQ.hide().appendTo("#message_show").slideDown(500);
    /**3秒之后自动删除生成的元素*/
    window.setTimeout(function () {
        messageJQ.slideUp("slow", function () {
            messageJQ.remove();
        })
    }, 2000);
}

var data = {pre_text: "** 原文 **", trans_text: "** 译文 **"}
var vm = new Vue({
    el: '#translate_show',
    data: data
})

$("#translate_close_btn").click(function () {
    $("#translate_show").hide()
});

function translate(text) {
    var appid = '20210111000668489';
    var key = 'XP9oeg7cfrADX3Rf9dGc';
    var salt = (new Date).getTime();
    var query = text;
    // 多个query可以用\n连接  如 query='apple\norange\nbanana\npear'
    var from = 'en';
    var to = 'zh';
    var str1 = appid + query + salt + key;
    var sign = md5(str1);
    $.ajax({
        url: 'http://api.fanyi.baidu.com/api/trans/vip/translate',
        type: 'get',
        dataType: 'jsonp',
        data: {
            q: query,
            appid: appid,
            salt: salt,
            from: from,
            to: to,
            sign: sign
        },
        success: function (data) {
            console.log(data);
            vm.trans_text = data["trans_result"][0]["dst"]
        }
    });
}

var $div = $("div#translate_show");
/* 绑定鼠标左键按住事件 */
$div.bind("mousedown", function (event) {
    /* 获取需要拖动节点的坐标 */
    var offset_x = $(this)[0].offsetLeft;//x坐标
    var offset_y = $(this)[0].offsetTop;//y坐标
    /* 获取当前鼠标的坐标 */
    var mouse_x = event.pageX;
    var mouse_y = event.pageY;
    /* 绑定拖动事件 */
    /* 由于拖动时，可能鼠标会移出元素，所以应该使用全局（document）元素 */
    $(document).bind("mousemove", function (ev) {
        // 计算鼠标移动了的位置
        var _x = ev.pageX - mouse_x;
        var _y = ev.pageY - mouse_y;
        /* 设置移动后的元素坐标 */
        var now_x = (offset_x + _x) + "px";
        var now_y = (offset_y + _y) + "px";
        /* 改变目标元素的位置 */
        $div.css({
            top: now_y,
            left: now_x
        });
    });
});
/* 当鼠标左键松开，接触事件绑定 */
$(document).bind("mouseup", function () {
    $(this).unbind("mousemove");
});


$('#viewerContainer').mouseup(function () {
    // var txt = window.getSelection?window.getSelection():document.selection.createRange().text;
    var txt = window.getSelection().toString()
    if (txt.length > 0) {
        console.log(txt);
        if (vm.pre_text != txt) {
            $("#translate_show").show()
            vm.pre_text = txt;
            vm.trans_text = "正在翻译中...";
            translate(txt);
        }

    }
})
var clipboard = new ClipboardJS(".btn_copy");
/*复制原文和译文*/
$("#trans_text").click(function () {
    $("#input_copy").val(vm.trans_text);
    $(".btn_copy").click();
    showCopyMessage("已复制译文", 0);
});

$("#pre_text").click(function () {
    $("#input_copy").val(vm.pre_text);
    $(".btn_copy").click();
    showCopyMessage("已复制原文", 1);
});

// 禁止网页缩放
const keyCodeMap = {
    // 91: true, // command
    61: true,
    107: true, // 数字键盘 +
    109: true, // 数字键盘 -
    173: true, // 火狐 - 号
    187: true, // +
    189: true, // -
};
// 覆盖ctrl||command + ‘+’/‘-’
document.onkeydown = function (event) {
    const e = event || window.event;
    const ctrlKey = e.ctrlKey || e.metaKey;
    if (ctrlKey && keyCodeMap[e.keyCode]) {
        e.preventDefault();
    } else if (e.detail) { // Firefox
        event.returnValue = false;
    }
};
// 覆盖鼠标滑动
document.body.addEventListener('wheel', (e) => {
    if (e.ctrlKey) {
        if (e.deltaY < 0) {
            e.preventDefault();
            return false;
        }
        if (e.deltaY > 0) {
            e.preventDefault();
            return false;
        }
    }
}, {passive: false});

function getQueryVariable(variable) {
    let query = window.location.href;
    let vars = query.split("&");
    for (let i = 0; i < vars.length; i++) {
        let pair = vars[i].split("=");
        if (pair[0] === variable) {
            return pair[1];
        }
    }
    return false;
}


// 保存进度
console.log(getQueryVariable("user_Token"))
console.log(getQueryVariable("paper_ID"))
let pageNumber_flag = $("#pageNumber").val()
setInterval(function () {
    if (pageNumber_flag !== $("#pageNumber").val()) {
        pageNumber_flag = $("#pageNumber").val()
        $.ajax({
            url: "/paper/paper_read_update", data: {
                "user_Token": getQueryVariable("user_Token"),
                "paper_ID": getQueryVariable("paper_ID"),
                "read_process": pageNumber_flag,
                "read_zoom": 100,
                "add_type": 1
            }, success: function () {
                console.log("ok")
            }
        });
    }
}, 1000)

