import xadmin
from .models import *


class ToDoListXadmin(object):  # 待办基础数据库
    list_display = ["sub_user", "valid_time", "content", "is_complete"]
    search_fields = ["sub_user", "valid_time", "content", "is_complete"]
    list_filter = ["sub_user", "valid_time", "content", "is_complete"]
    model_icon = "fa fa-check-square-o"


xadmin.site.register(ToDoList, ToDoListXadmin)


class TemplateForTODOmanageXadmin(object):  # 模板管理数据库
    list_display = ["sub_user", "name", "describe", "is_shared", "add_time"]
    search_fields = ["sub_user", "name", "describe", "is_shared", "add_time"]
    list_filter = ["sub_user", "name", "describe", "is_shared", "add_time"]
    model_icon = "fa fa-tags"


xadmin.site.register(TemplateForTODOmanage, TemplateForTODOmanageXadmin)


class ToDoListTemplateXadmin(object):  # TODO的模板
    list_display = ["sub_template", "sub_user", "content", "add_time"]
    search_fields = ["sub_template", "sub_user", "content", "add_time"]
    list_filter = ["sub_template", "sub_user", "content", "add_time"]
    model_icon = "fa fa-tag"


xadmin.site.register(ToDoListTemplate, ToDoListTemplateXadmin)


class ToDoListLogXadmin(object):  # TODO的模板
    list_display = ["sub_user", "content", "add_time"]
    search_fields = ["sub_user", "content", "add_time"]
    list_filter = ["sub_user", "content", "add_time"]
    model_icon = "fa fa-backward"


xadmin.site.register(ToDoListLog, ToDoListLogXadmin)
