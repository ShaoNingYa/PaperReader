import xadmin
from .models import *


class PaperConferenceXadmin(object):  # 存储会议
    list_display = ["name", "add_time"]
    search_fields = ["name", "add_time"]
    list_filter = ["name", "add_time"]
    model_icon = "fa fa-link"


class PaperBaseManageXadmin(object):
    list_display = ["name", "author", "sub_user", "conference", "conference_year", "paper_file", "add_time"]
    search_fields = ["name", "author", "sub_user", "conference", "conference_year", "paper_file", "add_time"]
    list_filter = ["name", "author", "sub_user", "conference", "conference_year", "paper_file", "add_time"]
    model_icon = "fa fa-th-list"


class PaperKeywordXadmin(object):  # 存储论文关键字
    list_display = ["keyword", "add_time"]
    search_fields = ["keyword", "add_time"]
    list_filter = ["keyword", "add_time"]
    model_icon = "fa fa-key"


class PaperKeywordConnectXadmin(object):  # 存储论文关键字中的联系
    list_display = ["paper_name", "keyword", "add_time"]
    search_fields = ["paper_name", "keyword", "add_time"]
    list_filter = ["paper_name", "keyword", "add_time"]
    model_icon = "fa fa-refresh"


class PaperLabelXadmin(object):  # 存储论文关键字
    list_display = ["sub_user", "label_text", "add_time"]
    search_fields = ["sub_user", "label_text", "add_time"]
    list_filter = ["sub_user", "label_text", "add_time"]
    model_icon = "fa fa-key"


class PaperLabelConnectXadmin(object):  # 存储论文关键字
    list_display = ["sub_user", "sub_paper", "sub_label", "add_time"]
    search_fields = ["sub_user", "sub_paper", "sub_label", "add_time"]
    list_filter = ["sub_user", "sub_paper", "sub_label", "add_time"]
    model_icon = "fa fa-key"


class PaperReviewManageXadmin(object):  # 评论
    list_display = ["paper_name", "sub_user", "starts", "review_text", "add_time"]
    search_fields = ["paper_name", "sub_user", "starts", "review_text", "add_time"]
    list_filter = ["paper_name", "sub_user", "starts", "review_text", "add_time"]
    model_icon = "fa fa-comments-o"


class PaperTransCodeManageXadmin(object):  # 翻译和代码(原论文的代码)
    list_display = ["paper_name", "sub_user", "add_time", "trans_file"]
    search_fields = ["paper_name", "sub_user", "add_time", "trans_file"]
    list_filter = ["paper_name", "sub_user", "add_time", "trans_file"]
    model_icon = "fa fa-exchange"


class PaperReadManageXadmin(object):  # 论文的浏览
    list_display = ["paper_name", "sub_user", "add_time", "add_type", "read_process", "read_zoom"]
    search_fields = ["paper_name", "sub_user", "add_time", "add_type", "read_process", "read_zoom"]
    list_filter = ["paper_name", "sub_user", "add_time", "add_type", "read_process", "read_zoom"]
    model_icon = "fa fa-check-square-o"


class PaperCodeManageXadmin(object):  # 根据论文，用户自己编写的代码
    list_display = ["paper_name", "sub_user", "add_time", "add_version"]
    search_fields = ["paper_name", "sub_user", "add_time", "add_version"]
    list_filter = ["paper_name", "sub_user", "add_time", "add_version"]
    model_icon = "fa fa-code"


xadmin.site.register(PaperConference, PaperConferenceXadmin)
xadmin.site.register(PaperBaseManage, PaperBaseManageXadmin)
xadmin.site.register(PaperKeyword, PaperKeywordXadmin)
xadmin.site.register(PaperKeywordConnect, PaperKeywordConnectXadmin)
xadmin.site.register(PaperReviewManage, PaperReviewManageXadmin)
xadmin.site.register(PaperTransCodeManage, PaperTransCodeManageXadmin)
xadmin.site.register(PaperReadManage, PaperReadManageXadmin)
xadmin.site.register(PaperCodeManage, PaperCodeManageXadmin)
xadmin.site.register(PaperLabel, PaperLabelXadmin)
xadmin.site.register(PaperLabelConnect, PaperLabelConnectXadmin)
