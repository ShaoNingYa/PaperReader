"""PaperReader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
import xadmin

urlpatterns = [
    # path(r'', xadmin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('admin/', admin.site.urls),
    path('study/', include("app_study_view.urls")),
    path('activities/', include("app_activities_view.urls")),
    path('paper/', include("app_paper_view.urls")),
    path('user/', include("app_user_manage.urls")),
]
urlpatterns += static('/statics/', document_root=settings.STATIC_ROOT)
