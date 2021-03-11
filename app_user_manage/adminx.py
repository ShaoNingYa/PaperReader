import time
import xadmin
from xadmin import views
from .models import EmailVerifyCode, UserProfile


class GlobalXadminSetting(object):
    site_title = "论文学习后台管理系统"
    site_footer = time.strftime("%Y-%m-%d")
    menu_style = "accordion"


class UserProfileXadmin(object):
    # list_display = ["image", "nick_name", "birthday", "gender", "user_type", "address", "phone"]
    # list_display = ["id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "email",
    #                 "is_staff", "is_active", "date_joined", "image", "nick_name", "birthday", "gender", "user_type",
    #                 "address", "phone", "add_time"]
    list_display = ["last_login", "is_superuser", "username", "email",
                    "is_staff", "is_active", "image", "nick_name", "birthday", "gender", "user_type",
                    "address", "phone"]
    search_fields = ["image", "nick_name", "birthday", "gender", "user_type", "address", "phone"]
    list_filter = ["image", "nick_name", "birthday", "gender", "user_type", "address", "phone"]


class EmailVerifyCodeXadmin(object):
    list_display = ["code", "email", "send_type", "add_time"]
    search_fields = ["code", "email", "send_type", "add_time"]
    list_filter = ["code", "email", "send_type", "add_time"]


xadmin.site.unregister(UserProfile)

xadmin.site.register(UserProfile, UserProfileXadmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeXadmin)
xadmin.site.register(views.CommAdminView, GlobalXadminSetting)
