from django.urls import path, re_path
from app_study_view import views
urlpatterns = [
    re_path(r'todolist_get_today', views.todolist_get_today, ),
    re_path(r"", views.index, ),
]
