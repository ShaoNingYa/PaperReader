from django.urls import path, re_path
from app_user_manage import views
urlpatterns = [
    re_path(r"login", views.login, ),
    re_path(r"info", views.info, ),
    re_path(r"logout", views.logout, ),
    re_path(r"", views.index, ),
]
