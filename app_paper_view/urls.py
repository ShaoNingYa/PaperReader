from django.urls import path, re_path
from app_paper_view import views
urlpatterns = [
    # re_path(r'api_test', views.getAllConferenceName, ),
    re_path(r'history_by_paperID', views.history_one_paper, ),
    re_path(r'history', views.history, ),
    re_path(r'paper_mine', views.paper_mine, ),
    re_path(r'paper_conference', views.paper_conference, ),
    re_path(r'paper_upload_file', views.paper_upload_file, ),
    re_path(r'get_all_conference', views.get_all_conference, ),
    re_path(r'get_all_label', views.get_all_label, ),
    re_path(r'get_conference_id_by_name', views.get_conference_id_by_name, ),
    re_path(r'get_label_id_by_name', views.get_label_id_by_name, ),
    re_path(r'paper_update', views.paper_update, ),
    re_path(r'paper_read_update', views.paper_read_update, ),
    re_path(r"", views.index, ),
]
