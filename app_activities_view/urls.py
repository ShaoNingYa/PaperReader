from django.urls import path, re_path
from app_activities_view import views
urlpatterns = [
    re_path(r'order_get_all', views.order_get_all, ),
    re_path(r'order_pic_upload', views.order_pic_upload, ),
    re_path(r'order_one_del', views.order_one_del, ),
    re_path(r"", views.index, ),
]
