from django.urls import path, re_path
from app_study_view import views
urlpatterns = [
    re_path(r'todolist_get_today', views.todolist_get_today, ),
    re_path(r'todolist_update_today', views.todolist_update_today, ),
    re_path(r'todolist_get_history', views.todolist_get_history, ),
    re_path(r'todolist_get_template', views.todolist_get_template, ),
    re_path(r'todolist_update_template', views.todolist_update_template, ),
    re_path(r"", views.index, ),
]
