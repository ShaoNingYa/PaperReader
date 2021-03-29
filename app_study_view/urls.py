from django.urls import path, re_path
from app_study_view import views
urlpatterns = [
    # re_path(r'api_test', views.getAllConferenceName, ),
    re_path(r"", views.index, ),
]
