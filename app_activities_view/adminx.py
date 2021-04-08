import xadmin
from .models import *


class BadmintonOrderXadmin(object):  # 待办基础数据库
    list_display = ["sub_user", "number_of_venue", "date_of_order", "time_quantum", "time_of_order", "pic_of_order", "remarks", "add_time"]
    search_fields = ["sub_user", "number_of_venue", "date_of_order", "time_quantum", "time_of_order", "pic_of_order", "remarks", "add_time"]
    list_filter = ["sub_user", "number_of_venue", "date_of_order", "time_quantum", "time_of_order", "pic_of_order", "remarks", "add_time"]
    model_icon = "fa fa-github-alt"


xadmin.site.register(BadmintonOrder, BadmintonOrderXadmin)
