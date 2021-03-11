"""codeManageAndShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app_selfPart.views import app_selfPart_main
from app_selfPart.views import app_selfPart_getCodeSimple
from app_selfPart.views import app_selfPart_getDynamicForAllFocus
from app_selfPart.views import app_selfPart_getDynamicForMySelf
from app_selfPart.views import app_selfPart_message
from app_selfPart.views import app_selfPart_getOnePersonMessage
from app_selfPart.views import app_selfPart_messageWrite
from app_selfPart.views import app_selfPart_messageGetNewAll
from app_selfPart.views import app_selfPart_messageRemoveNewOne
from app_selfPart.views import app_selfPart_messageClear
from app_selfPart.views import app_selfPart_changePassword
from app_selfPart.views import app_selfPart_changeUserPic
from app_selfPart.views import app_selfPart_messageGetUserIDByStudyNumber

from app_selfPart.views import app_selfPart_other
from app_selfPart.views import app_selfPart_getDynamicForOtherSelf
from app_selfPart.views import app_selfPart_getCodeSimpleOther
from app_selfPart.views import app_selfPart_other_addFriend
from app_selfPart.views import app_selfPart_other_delFriend
from app_selfPart.views import app_selfPart_other_addFocus
from app_selfPart.views import app_selfPart_other_delFocus

from app_selfPart.views import app_indexPart_topSearchByAjaxGetResult

from app_codeManage.views import codeManage_selfPartAddNewProjectGetIndex
from app_codeManage.views import codeManage_selfPartAddNewVersionGetIndex
from app_codeManage.views import codeManage_selfPartOneVersionGetIndex
from app_codeManage.views import codeManage_selfPartOneVersionGetIndex_returnPath
from app_codeManage.views import codeManage_selfPartOneProjectGetIndex
from app_codeManage.views import codeManage_getCodeCompare
from app_codeManage.views import codeManage_getCodeCompare_ChangeDetil
from app_codeManage.views import codeManage_addOneCodeTag
from app_codeManage.views import codeManageUploadAjax
from app_codeManage.views import codeManageUploadAjaxNewVersion

from app_codeManage.views import codeManage_allPartCodeSelectAndShow
from app_codeManage.views import codeManage_allPartCodeSelectAndShowAjaxGetCode

from app_codeManage.views import main_showIndex
from app_codeManage.views import main_showIndex_getHotTag

from app_codeManage.views import codeManage_oneCodeFileShow
from app_codeManage.views import codeManage_oneCodeFileShowForProjectShow

from app_codeManage.views import codeManage_deleteOneVersion

from app_codeManage.views import codeManage_getAllDiscuss
from app_codeManage.views import codeManage_getAllDiscussForWriteToDB
from app_codeManage.views import codeManage_getNewestDiscuss
from app_codeManage.views import codeManage_getHotestCode

from app_register.views import app_register
from app_register.views import app_register_infowrite
from app_register.views import ajax_sendEmail
from app_login.views import app_login
from app_login.views import app_logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'selfPart/$',app_selfPart_main),
    url(r'selfPart/index.html$',app_selfPart_main),
    url(r'selfPart/getCodeSimple$',app_selfPart_getCodeSimple),
    url(r'selfPart/getDynamicForAllFocus$',app_selfPart_getDynamicForAllFocus),
    url(r'selfPart/getDynamicForMySelf$',app_selfPart_getDynamicForMySelf),
    url(r'selfPart/message.html$',app_selfPart_message),
    url(r'selfPart/getOneMessage$',app_selfPart_getOnePersonMessage),
    url(r'selfPart/messageWrite$',app_selfPart_messageWrite),
    url(r'selfPart/messageGetNewAll$',app_selfPart_messageGetNewAll),
    url(r'selfPart/messageRemoveNewOne$',app_selfPart_messageRemoveNewOne),
    url(r'selfPart/messageClear$',app_selfPart_messageClear),
    url(r'selfPart/changePassword$',app_selfPart_changePassword),
    url(r'selfPart/changeUserPic$',app_selfPart_changeUserPic),
    url(r'selfPart/message/getUserIDByStudyNumber$',app_selfPart_messageGetUserIDByStudyNumber),

    url(r'index/topSearchByAjaxGetResult$',app_indexPart_topSearchByAjaxGetResult),

    url(r'otherPart/$',app_selfPart_other),
    url(r'otherPart/getDynamic$',app_selfPart_getDynamicForOtherSelf),
    url(r'otherPart/getCodeSimple$',app_selfPart_getCodeSimpleOther),
    
    url(r'otherPart/addFriend$',app_selfPart_other_addFriend),
    url(r'otherPart/delFriend$',app_selfPart_other_delFriend),
    url(r'otherPart/addFocus$',app_selfPart_other_addFocus),
    url(r'otherPart/delFocus$',app_selfPart_other_delFocus),

    url(r'selfPart/codeAddNewProject$',codeManage_selfPartAddNewProjectGetIndex),
    url(r'selfPart/codeAddNewVersion$',codeManage_selfPartAddNewVersionGetIndex),
    url(r'selfPart/codeOneVersion$',codeManage_selfPartOneVersionGetIndex),
    url(r'selfPart/codeOneVersionGetNextDir$',codeManage_selfPartOneVersionGetIndex_returnPath),
    url(r'selfPart/codeOneProject$',codeManage_selfPartOneProjectGetIndex),
    url(r'selfPart/getCodeCompare$',codeManage_getCodeCompare),
    url(r'selfPart/getCodeCompare_ChangeDetil$',codeManage_getCodeCompare_ChangeDetil),
    url(r'selfPart/addOneCodeTag$',codeManage_addOneCodeTag),
    url(r'selfPart/codeManageUploadAjax$',codeManageUploadAjax),
    url(r'selfPart/codeManageUploadAjaxNewVersion$',codeManageUploadAjaxNewVersion),

    url(r'allUser/allPartCodeSelectAndShow$',codeManage_allPartCodeSelectAndShow),
    url(r'allUser/allPartCodeSelectAndShowAjaxGetCode$',codeManage_allPartCodeSelectAndShowAjaxGetCode),

    url(r'^$',main_showIndex),
    url(r'index$',main_showIndex),
    url(r'index/getHotTag$',main_showIndex_getHotTag),

    url(r'selfPart/codeOneFileShow$',codeManage_oneCodeFileShow),
    url(r'selfPart/codeOneFileShowForProject$',codeManage_oneCodeFileShowForProjectShow),

    url(r'selfPart/deleteOneVersion$',codeManage_deleteOneVersion),
    
    url(r'selfPart/getAllDiscuss$',codeManage_getAllDiscuss),
    url(r'selfPart/getAllDiscussForWriteToDB$',codeManage_getAllDiscussForWriteToDB),
    url(r'selfPart/getNewestDiscuss$',codeManage_getNewestDiscuss),
    url(r'selfPart/getHotestCode$',codeManage_getHotestCode),

    url(r'login/$',app_login),
    url(r'logout/$',app_logout),
    url(r'^register/$',app_register),
    url(r'^register/infowrite$',app_register_infowrite),
    url(r'^ajax_sendEmail/$',ajax_sendEmail,name='sendEmail'),

]
