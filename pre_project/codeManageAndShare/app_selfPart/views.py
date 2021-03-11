# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# import app_register.models as nomal_user
# import app_codeManage.models as codeManage
# from models import selfPartMessage
# from models import selfPartMyFriends
# from models import selfPartFocusRelation
# from models import selfPartUserDynamic
# from models import selfPartFocusRelation
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate, login, logout
# import os
# import sys
# import random
# import string
# import datetime
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# # Create your views here.
# @login_required  # 加上这个装饰器就是限制必须登录才能执行这个函数
# def app_selfPart_main(request):
#     print request.user.first_name
#     userSelfInfoObject=nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id)
#     userID=userSelfInfoObject#noUse
#     userSelfInfo={}
#     userSelfInfo["username"]=userSelfInfoObject.nomal_username
#     userSelfInfo["userpic"]=userSelfInfoObject.nomal_userImg
#     userSelfInfo["useremail"]=userSelfInfoObject.nomal_useremail
#     userSelfInfo["sex"]=("男" if str(userSelfInfoObject.nomal_usersex)=="man" else "女")
#     userSelfInfo["grade"]=str(userSelfInfoObject.nomal_usergradeclass).split("_")[0]
#     userSelfInfo["class"]=str(userSelfInfoObject.nomal_usergradeclass).split("_")[1]
#     userSelfInfo["studyNumber"]=str(userSelfInfoObject.nomal_usernumber)
#     userSelfInfo["createTime"]=str(request.user.date_joined)
#     #print userSelfInfo
#     return render(request,'selfPart.html',{'username':request.user.first_name,"userSelfInfo":userSelfInfo})
#
# @csrf_exempt
# def app_selfPart_messageGetUserIDByStudyNumber(request):
#     willGetUserNumber = str(request.POST.get("UserNumber"))
#     willGetUserID = nomal_user.nomal_user.objects.get(nomal_usernumber=willGetUserNumber).id
#     return JsonResponse(willGetUserID,safe=False)
#
# def app_selfPart_other(request):
#     isLogin=0
#     isFocus=0
#     isFriend=0
#     currentLoginUserID = 0
#     if request.user.is_authenticated():
#         isLogin=1
#         currentLoginUserID = nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id).id
#     currentCheckUserID=request.GET["userID"]
#     userSelfInfoObject=nomal_user.nomal_user.objects.get(id=currentCheckUserID)
#     userID=userSelfInfoObject#noUse
#     userSelfInfo={}
#     userSelfInfo["username"]=userSelfInfoObject.nomal_username
#     userSelfInfo["userpic"]=userSelfInfoObject.nomal_userImg
#     userSelfInfo["useremail"]=userSelfInfoObject.nomal_useremail
#     userSelfInfo["sex"]=("男" if str(userSelfInfoObject.nomal_usersex)=="man" else "女")
#     userSelfInfo["sexCall"]=("他" if str(userSelfInfoObject.nomal_usersex)=="man" else "她")
#     userSelfInfo["grade"]=str(userSelfInfoObject.nomal_usergradeclass).split("_")[0]
#     userSelfInfo["class"]=str(userSelfInfoObject.nomal_usergradeclass).split("_")[1]
#     userSelfInfo["studyNumber"]=str(userSelfInfoObject.nomal_usernumber)
#     # userSelfInfo["createTime"]=str(request.user.date_joined)
#     #print userSelfInfo
#     if str(currentLoginUserID)==currentCheckUserID:
#         return render(request,'selfPart.html',{'username':request.user.first_name,"userSelfInfo":userSelfInfo})
#     #关注：
#     if selfPartFocusRelation.objects.all().filter(selfPartFocusRelationOwnID=currentLoginUserID,selfPartFocusRelationUserID=currentCheckUserID).exists():
#         isFocus=1
#     if selfPartMyFriends.objects.all().filter(selfPartOwnID=currentLoginUserID,selfPartFriendID=currentCheckUserID).exists():
#         isFriend=1
#     userID={"currentLoginUserID":currentLoginUserID,"currentCheckUserID":currentCheckUserID}
#     return render(request,'selfPartOther.html',{'username':userSelfInfo["username"],"userSelfInfo":userSelfInfo,"isLogin":isLogin,"isFocus":isFocus,"isFriend":isFriend,"userID":userID})
#
# @csrf_exempt
# def app_selfPart_other_addFriend(request):
#     currentLoginUserID=str(request.POST.get("currentLoginUserID"))
#     currentCheckUserID=str(request.POST.get("currentCheckUserID"))
#     addFriendObject = selfPartMyFriends(selfPartOwnID=currentLoginUserID,selfPartFriendID=currentCheckUserID)
#     addFriendObject.save()
#     return JsonResponse("添加好友成功",safe=False)
# @csrf_exempt
# def app_selfPart_other_delFriend(request):
#     currentLoginUserID=str(request.POST.get("currentLoginUserID"))
#     currentCheckUserID=str(request.POST.get("currentCheckUserID"))
#     addFriendObject = selfPartMyFriends.objects.all().filter(selfPartOwnID=currentLoginUserID,selfPartFriendID=currentCheckUserID)
#     addFriendObject.delete()
#     return JsonResponse("删除好友成功",safe=False)
#
# @csrf_exempt
# def app_selfPart_other_addFocus(request):
#     currentLoginUserID=str(request.POST.get("currentLoginUserID"))
#     currentCheckUserID=str(request.POST.get("currentCheckUserID"))
#     addFocusObject = selfPartFocusRelation(selfPartFocusRelationOwnID=currentLoginUserID,selfPartFocusRelationUserID=currentCheckUserID)
#     addFocusObject.selfPartFocusRelationCodeID = 0
#     addFocusObject.save()
#     return JsonResponse("关注成功",safe=False)
# @csrf_exempt
# def app_selfPart_other_delFocus(request):
#     currentLoginUserID=str(request.POST.get("currentLoginUserID"))
#     currentCheckUserID=str(request.POST.get("currentCheckUserID"))
#     addFocusObject = selfPartFocusRelation.objects.all().filter(selfPartFocusRelationOwnID=currentLoginUserID,selfPartFocusRelationUserID=currentCheckUserID)
#     addFocusObject.delete()
#     return JsonResponse("取消关注成功",safe=False)
#
# @csrf_exempt
# def app_selfPart_getDynamicForOtherSelf(request):
#     #这个函数的功能是返回当前用户的动态
#     selfPartUserDynamicUserID=str(request.POST.get("userID"))
#     # selfPartUserDynamicUserID=str(nomal_user.nomal_user.objects.all().filter(nomal_usernumber="140104010034")[0].id)
#     selfPartUserDynamicAlls = selfPartUserDynamic.objects.all().filter(selfPartUserDynamicUserID=selfPartUserDynamicUserID).order_by('-selfPartUserDynamicTime')
#     dynamicAll=[]
#     for selfPartUserDynamicAll in selfPartUserDynamicAlls:
#         # print "传递一条动态"
#         selfPartUserDynamicCodeName = codeManage.codeManage.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicCodeID)[0].codeManageCodeName
#         selfPartUserDynamicExplain = codeManage.codeManage.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicCodeID)[0].codeManageCodeExplain
#         dynamic={
#             "id":selfPartUserDynamicAll.id,
#             "selfPartUserDynamicType":selfPartUserDynamicAll.selfPartUserDynamicType,
#             "selfPartUserDynamicPic":selfPartUserDynamicAll.selfPartUserDynamicPic,
#             # "selfPartUserDynamicExplain":selfPartUserDynamicAll.selfPartUserDynamicExplain,
#             "selfPartUserDynamicExplain":selfPartUserDynamicExplain,
#             "selfPartUserDynamicCodeID":selfPartUserDynamicAll.selfPartUserDynamicCodeID,
#             "selfPartUserDynamicCodeSecondNumber":codeManage.codeManage.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicCodeID)[0].codeManageSecondNumber,
#             "selfPartUserDynamicCodeName":selfPartUserDynamicCodeName,
#             "selfPartUserDynamicTime":str(selfPartUserDynamicAll.selfPartUserDynamicTime),
#         }
#         dynamicAll.append(dynamic)
#     return JsonResponse(dynamicAll,safe=False)
#
# @csrf_exempt
# def app_selfPart_getCodeSimpleOther(request):
#     allCodeFirstNumbers=[]
#     selfPartAllCodeSimpleOnes = {}
#     selfPartAllCodeSimpleOnesPush = {}
#     selfPartAllCodeSimpleOnesPushOne = {}
#     selfPartAllCodeSimpleOnesPushOneOne = {}
#     allCodeSimples=[]
#     selfPartUserID=str(request.POST.get("userID"))
#     selfPartAllCodeSimples = codeManage.codeManage.objects.all().filter(codeManageIsShare=True).filter(codeManageCodeAuthor=selfPartUserID)
#     for selfPartAllCodeSimpleForFirstNumber in selfPartAllCodeSimples:
#         allCodeFirstNumbers.append(selfPartAllCodeSimpleForFirstNumber.codeManageFirstNumber)
#     allCodeFirstNumbers = list(set(allCodeFirstNumbers))    #去重
#     # print allCodeFirstNumbers
#     # 思路：先从数据库中将本用户的所有程序取出，然后根据主版本号进行分类
#     for allCodeFirstNumber in allCodeFirstNumbers:
#         selfPartAllCodeSimpleOnes[allCodeFirstNumber] = selfPartAllCodeSimples.filter(codeManageFirstNumber=allCodeFirstNumber).order_by("-codeManageUploadTime")
#     # print selfPartAllCodeSimpleOnes #{FirstNumber:QuerySet}
#     for selfPartAllCodeCodeFirstNumberIndex in selfPartAllCodeSimpleOnes:
#         # print "selfPartAllCodeCodeFirstNumberIndex:"+selfPartAllCodeCodeFirstNumberIndex
#         selfPartAllCodeSimpleOnesPushOne["codeFirstNumber"] = selfPartAllCodeCodeFirstNumberIndex
#         for selfPartAllCodeSimpleOne in selfPartAllCodeSimpleOnes[selfPartAllCodeCodeFirstNumberIndex]:
#             # print selfPartAllCodeSimpleOne.codeManageSecondNumber
#             #############下面是获取标签：
#             getCodeID = selfPartAllCodeSimpleOne.id
#             getAllRelations = codeManage.codeTagRelation.objects.all().filter(codeTagRelationiCodeID=getCodeID)
#             getAllTags = []
#             for getAllRelation in getAllRelations:
#                 # print getAllRelation.codeTagRelationTagID
#                 getAllTags.append(codeManage.codeTag.objects.all().filter(id=getAllRelation.codeTagRelationTagID)[0].codeTagName)
#             # print getAllTags
#             #############下面是产生传往前台的数据：
#             selfPartAllCodeSimpleOnesPushOneOne["codeSecondNumber"] = selfPartAllCodeSimpleOne.codeManageSecondNumber
#             selfPartAllCodeSimpleOnesPushOneOne["codeName"] = selfPartAllCodeSimpleOne.codeManageCodeName
#             selfPartAllCodeSimpleOnesPushOneOne["codeAllTags"] = getAllTags
#             selfPartAllCodeSimpleOnesPushOneOne["codeIsShare"] = selfPartAllCodeSimpleOne.codeManageIsShare
#             selfPartAllCodeSimpleOnesPushOneOne["codeLanguage"] = codeManage.codeLanguage.objects.all().filter(id=selfPartAllCodeSimpleOne.codeManageLanguage)[0].codeLanguageType
#             selfPartAllCodeSimpleOnesPushOneOne["codeSerchTimes"] = selfPartAllCodeSimpleOne.codeManageSearchTimes
#             selfPartAllCodeSimpleOnesPushOneOne["codeCheckTimes"] = selfPartAllCodeSimpleOne.codeManageCheckTimes
#             selfPartAllCodeSimpleOnesPushOneOne["codeDownloadTimes"] = selfPartAllCodeSimpleOne.codeManageDownloadTimes
#             selfPartAllCodeSimpleOnesPushOneOne["codeExplain"] = selfPartAllCodeSimpleOne.codeManageCodeExplain
#             selfPartAllCodeSimpleOnesPushOneOne["codeUploadTime"] = str(selfPartAllCodeSimpleOne.codeManageUploadTime)
#             selfPartAllCodeSimpleOnesPushOne[selfPartAllCodeSimpleOne.codeManageSecondNumber] = selfPartAllCodeSimpleOnesPushOneOne.copy()
#             # print selfPartAllCodeSimpleOnesPushOne
#         selfPartAllCodeSimpleOnesPush[selfPartAllCodeCodeFirstNumberIndex]=selfPartAllCodeSimpleOnesPushOne.copy()
#         # selfPartAllCodeSimpleOnesPush.append(selfPartAllCodeSimpleOnesPushOne)
#         # print selfPartAllCodeSimpleOnesPush
#         selfPartAllCodeSimpleOnesPushOne={}
#     # print selfPartAllCodeSimpleOnes
#     # print selfPartAllCodeSimpleOnesPush
#     return JsonResponse(selfPartAllCodeSimpleOnesPush,safe=False)
#
# @login_required  # 加上这个装饰器就是限制必须登录才能执行这个函数
# def app_selfPart_message(request):
#     thisUserObject=nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id)
#     userID=thisUserObject.id
#     allFriends=selfPartMyFriends.objects.all().filter(selfPartOwnID=userID)
#     myFriendOneAlls=[]
#     for allFriend in allFriends:
#         # print "myfriend:" + str(allFriend.selfPartFriendID)
#         myFriendOneAlls.append(nomal_user.nomal_user.objects.get(id=allFriend.selfPartFriendID))
#     # for myFriendOneAll in myFriendOneAlls:
#     #     print myFriendOneAll.nomal_username
#     #     print myFriendOneAll.nomal_usernumber
#     #     print myFriendOneAll.nomal_userImg
#     #获取历史消息
#     allSendMessages=selfPartMessage.objects.all().filter(selfPartMessageSendUserID=userID,selfPartMessageIsDeleteBySend=False)
#     allReceMessages=selfPartMessage.objects.all().filter(selfPartMessageReceUserID=userID,selfPartMessageIsDeleteByRece=False)
#     allMessageUserIDs=[]
#     allMessageSendAlls=[]
#     allMessageReceAlls=[]
#     for allReceMessage in allReceMessages:
#         # print "allReceMessageId:"+str(allReceMessage.selfPartMessageSendUserID)
#         allMessageUserIDs.append(allReceMessage.selfPartMessageSendUserID)
#     for allSendMessage in allSendMessages:
#         # print "allSendMessageId:"+str(allSendMessage.selfPartMessageReceUserID)
#         allMessageUserIDs.append(allSendMessage.selfPartMessageReceUserID)
#     allMessageUserIDs=set(allMessageUserIDs)
#     # print allMessageUserIDs
#     allMessageFriends=[]
#     for allMessageUserID in allMessageUserIDs:
#         allMessageFriends.append(nomal_user.nomal_user.objects.get(id=allMessageUserID))
#     # for allMessageFriend in allMessageFriends:
#     #      print "聊天窗口正在聊天的用户名："+allMessageFriend.nomal_username
#     ##selfPartMessageAll.filter(selfPartMessageSendUserID=1,selfPartMessageReceUserID=3)[0].id
#     #allMessageOneAlls=[]
#     #for allMessage in allMessages:
#     #    print "Message:" + str(allMessage.selfPartFriendID)
#     #    myFriendOneAlls.append(nomal_user.nomal_user.objects.get(id=allFriend.selfPartFriendID))
#     #for myFriendOneAll in myFriendOneAlls:
#     #    print myFriendOneAll.nomal_username
#     #    print myFriendOneAll.nomal_usernumber
#     #    print myFriendOneAll.nomal_userImg
#     return render(request,'selfPart_message.html',{'username':request.user.first_name,'userpic':thisUserObject.nomal_userImg,"myFriendOneAlls":myFriendOneAlls,"allMessageFriends":allMessageFriends})
#
# def app_selfPart_getOnePersonMessage(request):
#     studyNumber=request.GET['studyNumber']
#     ######下########根据学号获取对应的聊天消息############
#     #studyNumber="140104010033"
#     userIDForMessageHistory=nomal_user.nomal_user.objects.get(nomal_usernumber=studyNumber).id
#     userIDCurrentUserID=nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id).id
#     #userIDCurrentUserID=nomal_user.nomal_user.objects.get(nomal_userconfirmid=10).id
#     # print "根据学号获取ID:"+str(userIDForMessageHistory)
#     # print "获取当前用户ID:"+str(userIDCurrentUserID)
#     thisSendMessages=selfPartMessage.objects.all().filter(selfPartMessageSendUserID=userIDForMessageHistory,selfPartMessageReceUserID=userIDCurrentUserID,selfPartMessageIsDeleteByRece=False)
#     thisReceMessages=selfPartMessage.objects.all().filter(selfPartMessageReceUserID=userIDForMessageHistory,selfPartMessageSendUserID=userIDCurrentUserID,selfPartMessageIsDeleteBySend=False)
#     thisMessages = thisSendMessages | thisReceMessages
#     thisMessagesOrder = thisMessages.order_by("selfPartMessageCreateTime")
#     oneMessages = []
#     for thisMessage in thisMessagesOrder:
#         #print dir(thisMessage)
#         oneMessages.append([thisMessage.selfPartMessageSendUserID,thisMessage.selfPartMessageReceUserID,thisMessage.selfPartMessageContent,str(thisMessage.selfPartMessageCreateTime)])
#         # print thisMessage.selfPartMessageSendUserID + " TO "  + thisMessage.selfPartMessageReceUserID + "  " + thisMessage.selfPartMessageContent + "  " + str(thisMessage.selfPartMessageCreateTime)[:-6]
#     oneMessages.append(userIDCurrentUserID)
#     ######上########根据学号获取对应的聊天消息############
#     #OneMessages = [[1,2,3],["a","b","c"]]
#     return JsonResponse(oneMessages,safe=False)
#
#
# @csrf_exempt
# def app_selfPart_messageWrite(request):
#     #这个函数的功能是将一条POST推送来的消息写入数据库，并返回成功与否
#     writeState="失败"
#     if request.method == "POST":
#         selfPartMessageReceUserNumber = request.POST.get("selfPartMessageReceUserID")
#         selfPartMessageContent = request.POST.get("selfPartMessageContent")
#         #print selfPartMessageReceUserID + selfPartMessageContent
#         # print "保存消息： "+request.user.username + "  " + selfPartMessageReceUserNumber
#         selfPartMessageSendUserID=str(nomal_user.nomal_user.objects.all().filter(nomal_usernumber=request.user.username)[0].id)
#         selfPartMessageReceUserID=str(nomal_user.nomal_user.objects.all().filter(nomal_usernumber=selfPartMessageReceUserNumber)[0].id)
#         # print "保存消息： ID: "+selfPartMessageSendUserID+ "  " + selfPartMessageReceUserID
#         oneMessageSave = selfPartMessage(selfPartMessageSendUserID=selfPartMessageSendUserID,selfPartMessageReceUserID=selfPartMessageReceUserID,selfPartMessageContent=selfPartMessageContent)
#         oneMessageSave.selfPartMessageIsNew=1
#         oneMessageSave.selfPartMessageIsDeleteBySend=False
#         oneMessageSave.selfPartMessageIsDeleteByRece=False
#         oneMessageSave.save()
#         writeState="成功"
#     return JsonResponse(writeState,safe=False)
#
# @csrf_exempt
# def app_selfPart_messageGetNewAll(request):
#     #这个函数的功能是从数据库中获取新的消息，返回有新消息的用户
#     allMessageUserIDs=[]
#     allMessageUserNumbers=[]
#     selfPartMessageSendUserID=str(nomal_user.nomal_user.objects.all().filter(nomal_usernumber=request.user.username)[0].id)
#     allSendMessages=selfPartMessage.objects.all().filter(selfPartMessageReceUserID=selfPartMessageSendUserID,selfPartMessageIsNew=1)
#     for allSendMessage in allSendMessages:
#         allMessageUserIDs.append(str(allSendMessage.selfPartMessageSendUserID))
#     for allMessageUserID in allMessageUserIDs:
#         allMessageUserNumbers.append(str(nomal_user.nomal_user.objects.all().filter(id=allMessageUserID)[0].nomal_usernumber))
#     # if allMessageUserNumbers:
#         # print allMessageUserNumbers
#     return JsonResponse(allMessageUserNumbers,safe=False)
#
# @csrf_exempt
# def app_selfPart_messageRemoveNewOne(request):
#     #这个函数的功能是将已经阅读的消息从数据库中进行标记
#     # print "已经阅读的学号"+request.POST.get("getAlreadyReadNumber")
#     selfPartMessageSendUserID=str(nomal_user.nomal_user.objects.all().filter(nomal_usernumber=request.POST.get("getAlreadyReadNumber"))[0].id)
#     selfPartMessage.objects.filter(selfPartMessageSendUserID=selfPartMessageSendUserID).update(selfPartMessageIsNew=0)
#     return JsonResponse("ok",safe=False)
#
#
# @csrf_exempt
# def app_selfPart_messageClear(request):
#     #这个函数的功能是清除历史记录
#     thatUserNumber = request.POST.get("thatUserNumber")
#     thisUserNumber = request.user.username
#     thatUserID = nomal_user.nomal_user.objects.all().filter(nomal_usernumber=thatUserNumber)[0].id
#     thisUserID = nomal_user.nomal_user.objects.all().filter(nomal_usernumber=thisUserNumber)[0].id
#     receMassageFilter = selfPartMessage.objects.all().filter(selfPartMessageSendUserID=thatUserID,selfPartMessageReceUserID=thisUserID)
#     receMassageFilter.update(selfPartMessageIsDeleteByRece=True)
#     SendMassageFilter = selfPartMessage.objects.all().filter(selfPartMessageSendUserID=thisUserID,selfPartMessageReceUserID=thatUserID)
#     SendMassageFilter.update(selfPartMessageIsDeleteBySend=True)
#     return JsonResponse("ok",safe=False)
#
#
# @csrf_exempt
# def app_selfPart_getDynamicForAllFocus(request):
#     #这个函数的功能是返回当前用户关注的所有用户的动态
#     selfPartUserDynamicUserID=str(nomal_user.nomal_user.objects.all().filter(nomal_usernumber=request.user.username)[0].id)
#     getFocusUserIDs = selfPartFocusRelation.objects.all().filter(selfPartFocusRelationOwnID=selfPartUserDynamicUserID)
#     selfPartUserDynamicAlls = selfPartUserDynamic.objects.all().filter(selfPartUserDynamicUserID=selfPartUserDynamicUserID)
#     for getFocusUserID in getFocusUserIDs:
#         selfPartUserDynamicAlls = selfPartUserDynamicAlls | selfPartUserDynamic.objects.all().filter(selfPartUserDynamicUserID=getFocusUserID.selfPartFocusRelationUserID)
#     selfPartUserDynamicAlls = selfPartUserDynamicAlls.order_by('-selfPartUserDynamicTime')
#     dynamicAll=[]
#     for selfPartUserDynamicAll in selfPartUserDynamicAlls:
#         # print "传递一条动态"
#         selfPartUserDynamicCodeName = codeManage.codeManage.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicCodeID)[0].codeManageCodeName
#         selfPartUserDynamicExplain = codeManage.codeManage.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicCodeID)[0].codeManageCodeExplain
#         getThisDynamicBelongUserName = nomal_user.nomal_user.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicUserID)[0].nomal_username
#         getThisDynamicBelongUserID = nomal_user.nomal_user.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicUserID)[0].id
#         getThisDynamicBelongUserPic = nomal_user.nomal_user.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicUserID)[0].nomal_userImg
#         dynamic={
#             "id":selfPartUserDynamicAll.id,
#             "selfPartUserDynamicType":selfPartUserDynamicAll.selfPartUserDynamicType,
#             "selfPartUserName":getThisDynamicBelongUserName,
#             "selfPartUserID":getThisDynamicBelongUserID,
#             "selfPartUserPic":getThisDynamicBelongUserPic,
#             "selfPartUserDynamicPic":selfPartUserDynamicAll.selfPartUserDynamicPic,
#             # "selfPartUserDynamicExplain":selfPartUserDynamicAll.selfPartUserDynamicExplain,
#             "selfPartUserDynamicExplain":selfPartUserDynamicExplain,
#             "selfPartUserDynamicCodeID":selfPartUserDynamicAll.selfPartUserDynamicCodeID,
#             "selfPartUserDynamicCodeSecondNumber":codeManage.codeManage.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicCodeID)[0].codeManageSecondNumber,
#             "selfPartUserDynamicCodeName":selfPartUserDynamicCodeName,
#             "selfPartUserDynamicTime":str(selfPartUserDynamicAll.selfPartUserDynamicTime),
#         }
#         dynamicAll.append(dynamic)
#     # print dynamicAll
#     return JsonResponse(dynamicAll,safe=False)
# @csrf_exempt
# def app_selfPart_getDynamicForMySelf(request):
#     #这个函数的功能是返回当前用户的动态
#     selfPartUserDynamicUserID=str(nomal_user.nomal_user.objects.all().filter(nomal_usernumber=request.user.username)[0].id)
#     # selfPartUserDynamicUserID=str(nomal_user.nomal_user.objects.all().filter(nomal_usernumber="140104010034")[0].id)
#     selfPartUserDynamicAlls = selfPartUserDynamic.objects.all().filter(selfPartUserDynamicUserID=selfPartUserDynamicUserID).order_by('-selfPartUserDynamicTime')
#     dynamicAll=[]
#     for selfPartUserDynamicAll in selfPartUserDynamicAlls:
#         # print "传递一条动态"
#         selfPartUserDynamicCodeName = codeManage.codeManage.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicCodeID)[0].codeManageCodeName
#         selfPartUserDynamicExplain = codeManage.codeManage.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicCodeID)[0].codeManageCodeExplain
#         dynamic={
#             "id":selfPartUserDynamicAll.id,
#             "selfPartUserDynamicType":selfPartUserDynamicAll.selfPartUserDynamicType,
#             "selfPartUserDynamicPic":selfPartUserDynamicAll.selfPartUserDynamicPic,
#             # "selfPartUserDynamicExplain":selfPartUserDynamicAll.selfPartUserDynamicExplain,
#             "selfPartUserDynamicExplain":selfPartUserDynamicExplain,
#             "selfPartUserDynamicCodeID":selfPartUserDynamicAll.selfPartUserDynamicCodeID,
#             "selfPartUserDynamicCodeSecondNumber":codeManage.codeManage.objects.all().filter(id=selfPartUserDynamicAll.selfPartUserDynamicCodeID)[0].codeManageSecondNumber,
#             "selfPartUserDynamicCodeName":selfPartUserDynamicCodeName,
#             "selfPartUserDynamicTime":str(selfPartUserDynamicAll.selfPartUserDynamicTime),
#         }
#         dynamicAll.append(dynamic)
#     return JsonResponse(dynamicAll,safe=False)
#
# @csrf_exempt
# def app_selfPart_getCodeSimple(request):
#     allCodeFirstNumbers=[]
#     selfPartAllCodeSimpleOnes = {}
#     selfPartAllCodeSimpleOnesPush = {}
#     selfPartAllCodeSimpleOnesPushOne = {}
#     selfPartAllCodeSimpleOnesPushOneOne = {}
#     allCodeSimples=[]
#     selfPartUserID=str(nomal_user.nomal_user.objects.all().filter(nomal_usernumber=request.user.username)[0].id)
#     selfPartAllCodeSimples = codeManage.codeManage.objects.all().filter(codeManageCodeAuthor=selfPartUserID,codeManageIsDelete=False)
#     for selfPartAllCodeSimpleForFirstNumber in selfPartAllCodeSimples:
#         allCodeFirstNumbers.append(selfPartAllCodeSimpleForFirstNumber.codeManageFirstNumber)
#     allCodeFirstNumbers = list(set(allCodeFirstNumbers))    #去重
#     # print allCodeFirstNumbers
#     # 思路：先从数据库中将本用户的所有程序取出，然后根据主版本号进行分类
#     for allCodeFirstNumber in allCodeFirstNumbers:
#         selfPartAllCodeSimpleOnes[allCodeFirstNumber] = selfPartAllCodeSimples.filter(codeManageFirstNumber=allCodeFirstNumber).order_by("-codeManageUploadTime")
#     # print selfPartAllCodeSimpleOnes #{FirstNumber:QuerySet}
#     for selfPartAllCodeCodeFirstNumberIndex in selfPartAllCodeSimpleOnes:
#         # print "selfPartAllCodeCodeFirstNumberIndex:"+selfPartAllCodeCodeFirstNumberIndex
#         selfPartAllCodeSimpleOnesPushOne["codeFirstNumber"] = selfPartAllCodeCodeFirstNumberIndex
#         for selfPartAllCodeSimpleOne in selfPartAllCodeSimpleOnes[selfPartAllCodeCodeFirstNumberIndex]:
#             # print selfPartAllCodeSimpleOne.codeManageSecondNumber
#             #############下面是获取标签：
#             getCodeID = selfPartAllCodeSimpleOne.id
#             getAllRelations = codeManage.codeTagRelation.objects.all().filter(codeTagRelationiCodeID=getCodeID)
#             getAllTags = []
#             for getAllRelation in getAllRelations:
#                 # print getAllRelation.codeTagRelationTagID
#                 getAllTags.append(codeManage.codeTag.objects.all().filter(id=getAllRelation.codeTagRelationTagID)[0].codeTagName)
#             # print getAllTags
#             #############下面是产生传往前台的数据：
#             selfPartAllCodeSimpleOnesPushOneOne["codeSecondNumber"] = selfPartAllCodeSimpleOne.codeManageSecondNumber
#             selfPartAllCodeSimpleOnesPushOneOne["codeName"] = selfPartAllCodeSimpleOne.codeManageCodeName
#             selfPartAllCodeSimpleOnesPushOneOne["codeAllTags"] = getAllTags
#             selfPartAllCodeSimpleOnesPushOneOne["codeIsShare"] = selfPartAllCodeSimpleOne.codeManageIsShare
#             selfPartAllCodeSimpleOnesPushOneOne["codeLanguage"] = codeManage.codeLanguage.objects.all().filter(id=selfPartAllCodeSimpleOne.codeManageLanguage)[0].codeLanguageType
#             selfPartAllCodeSimpleOnesPushOneOne["codeSerchTimes"] = selfPartAllCodeSimpleOne.codeManageSearchTimes
#             selfPartAllCodeSimpleOnesPushOneOne["codeCheckTimes"] = selfPartAllCodeSimpleOne.codeManageCheckTimes
#             selfPartAllCodeSimpleOnesPushOneOne["codeDownloadTimes"] = selfPartAllCodeSimpleOne.codeManageDownloadTimes
#             selfPartAllCodeSimpleOnesPushOneOne["codeExplain"] = selfPartAllCodeSimpleOne.codeManageCodeExplain
#             selfPartAllCodeSimpleOnesPushOneOne["codeUploadTime"] = str(selfPartAllCodeSimpleOne.codeManageUploadTime)
#             selfPartAllCodeSimpleOnesPushOne[selfPartAllCodeSimpleOne.codeManageSecondNumber] = selfPartAllCodeSimpleOnesPushOneOne.copy()
#             # print selfPartAllCodeSimpleOnesPushOne
#         selfPartAllCodeSimpleOnesPush[selfPartAllCodeCodeFirstNumberIndex]=selfPartAllCodeSimpleOnesPushOne.copy()
#         # selfPartAllCodeSimpleOnesPush.append(selfPartAllCodeSimpleOnesPushOne)
#         # print selfPartAllCodeSimpleOnesPush
#         selfPartAllCodeSimpleOnesPushOne={}
#     # print selfPartAllCodeSimpleOnes
#     # print selfPartAllCodeSimpleOnesPush
#     return JsonResponse(selfPartAllCodeSimpleOnesPush,safe=False)
#
#
#
#
# #下面是修改密码：
# @csrf_exempt
# def app_selfPart_changePassword(request):
#     changeResult="修改失败"
#     if request.method == "POST":
#         username = request.user.username
#         oldPassword = request.POST['oldPassword']
#         newPassword = request.POST['newPassword']
#         user = authenticate(username=username, password=oldPassword)
#         if user is not None:
#             print "认证成功"
#             if user.is_active:
#                 print "当前用户可用"
#                 user.set_password(newPassword)
#                 user.save()
#                 changeResult="修改成功"
#     print "修改密码结果： "+changeResult
#     return JsonResponse(changeResult,safe=False)
#
#
#
# #下面是修改头像：
# @csrf_exempt
# def app_selfPart_changeUserPic(request):
#     if request.method == 'POST':
#         getCurrentUserObject = nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id)
#         currentUserID = getCurrentUserObject.id
#         currentUserNumber = getCurrentUserObject.nomal_usernumber
#
#         #下面是上传文件
#         BASE_DIR = os.path.abspath('.')+"/common_static/selfPart/userImg/"+currentUserNumber
#         if not os.path.exists(BASE_DIR):
#             os.makedirs(BASE_DIR)
#         else:
#             print "目录已经存在"
#         file_obj = request.FILES.get('file')
#         f = open(os.path.join(BASE_DIR, file_obj.name), 'wb')
#         for chunk in file_obj.chunks():
#             f.write(chunk)
#         f.close()
#         userPicSavePosition = "/static/selfPart/userImg/" + currentUserNumber + "/" + file_obj.name
#         getCurrentUserObject.nomal_userImg = userPicSavePosition
#         getCurrentUserObject.save()
#         changeResult = "success"
#         return  JsonResponse(changeResult,safe=False)
#
# def check_contain_chinese(check_str):
#     #此函数的功能是判断一句话里是否有中文
#     for ch in check_str.decode('utf-8'):
#         if u'\u4e00' <= ch <= u'\u9fff':
#             return True
#     return False
#
# @csrf_exempt
# def app_indexPart_topSearchByAjaxGetResult(request):
#     #此函数的功能是根据传过来的数据在数据库中进行检索，然后将检索结果返回
#     keywords = request.POST.get("keywords")
#     # print keywords
#     userInfo = {}  #包含用户ID、用户名、检索原因
#     userInfoAll = []
#     codeInfo = {}  #
#     codeInfoAll = []
#     tagInfo = {}  #
#     tagInfoAll = []
#     if keywords.strip()!="":
#         #icontains
#             # 根据用户名的关键字  ===>  用户名（用户名）  ===>  用户主页
#         getUserByUserNameObjects = nomal_user.nomal_user.objects.all().filter(nomal_username__icontains=keywords)
#         for getUserByUserNameObject in getUserByUserNameObjects:
#             userInfo["userID"] = getUserByUserNameObject.id
#             userInfo["userName"] = getUserByUserNameObject.nomal_username
#             userInfo["getReason"] = "根据用户名："+getUserByUserNameObject.nomal_username
#             userInfoAll.append(userInfo.copy())
#             # 根据学号的关键字  ===>  用户名（全部学号）  ===>  用户主页
#         getUserByUserNumberObjects = nomal_user.nomal_user.objects.all().filter(nomal_usernumber__icontains=keywords)
#         for getUserByUserNumberObject in getUserByUserNumberObjects:
#             userInfo["userID"] = getUserByUserNumberObject.id
#             userInfo["userName"] = getUserByUserNumberObject.nomal_username
#             userInfo["getReason"] = "根据学号："+getUserByUserNumberObject.nomal_usernumber
#             userInfoAll.append(userInfo.copy())
#             # 根据年级班级的关键字  ===>  用户名（年级班级）  ===>  用户主页
#         getUserByUserGradeOrClassObjects = nomal_user.nomal_user.objects.all().filter(nomal_usergradeclass__icontains=keywords)
#         for getUserByUserGradeOrClassObject in getUserByUserGradeOrClassObjects:
#             userInfo["userID"] = getUserByUserGradeOrClassObject.id
#             userInfo["userName"] = getUserByUserGradeOrClassObject.nomal_username
#             userInfo["getReason"] = "根据年级班级："+getUserByUserGradeOrClassObject.nomal_usergradeclass.split("_")[0]+"级"+getUserByUserGradeOrClassObject.nomal_usergradeclass.split("_")[1]+"班"
#             userInfoAll.append(userInfo.copy())
#             # 根据邮箱的关键字  ===>  用户名（全部邮箱）  ===>  用户主页
#         getUserByUserEmailObjects = nomal_user.nomal_user.objects.all().filter(nomal_useremail__icontains=keywords)
#         for getUserByUserEmailObject in getUserByUserEmailObjects:
#             userInfo["userID"] = getUserByUserEmailObject.id
#             userInfo["userName"] = getUserByUserEmailObject.nomal_username
#             userInfo["getReason"] = "根据邮箱："+getUserByUserEmailObject.nomal_useremail
#             userInfoAll.append(userInfo.copy())
#             # 根据程序名字的关键字  ===>  程序名（全部程序名）  ===>  程序主页（仅显示工程）
#         getCodeByCodeNameObjects = codeManage.codeManage.objects.all().filter(codeManageMainFlag=1,codeManageIsDelete=False).filter(codeManageCodeName__icontains=keywords)
#         for getCodeByCodeNameObject in getCodeByCodeNameObjects:
#             codeInfo["codeFirstNumber"] = getCodeByCodeNameObject.codeManageFirstNumber
#             codeInfo["codeName"] = getCodeByCodeNameObject.codeManageCodeName
#             codeInfo["getReason"] = "根据程序名："+getCodeByCodeNameObject.codeManageCodeName
#             codeInfoAll.append(codeInfo.copy())
#             # 根据程序解释的关键字  ===>  程序名（全部解释）  ===>  程序主页（仅显示工程）
#         getCodeByCodeNameObjects = codeManage.codeManage.objects.all().filter(codeManageIsDelete=False).filter(codeManageCodeExplain__icontains=keywords)
#         for getCodeByCodeNameObject in getCodeByCodeNameObjects:
#             codeInfo["codeFirstNumber"] = getCodeByCodeNameObject.codeManageFirstNumber
#             codeInfo["codeName"] = getCodeByCodeNameObject.codeManageCodeName
#             codeInfo["getReason"] = "根据程序说明："+getCodeByCodeNameObject.codeManageCodeExplain
#             codeInfoAll.append(codeInfo.copy())
#             # 根据程序提交的时间  ===>  程序名（全部提交时间）  ===>  程序主页（显示工程|！单独的程序版本）
#         if not check_contain_chinese(keywords):
#             getCodeByCodeNameObjects = codeManage.codeManage.objects.all().filter(codeManageIsDelete=False).filter(codeManageMainFlag=1).filter(codeManageUploadTime__icontains=keywords)
#             for getCodeByCodeNameObject in getCodeByCodeNameObjects:
#                 codeInfo["codeFirstNumber"] = getCodeByCodeNameObject.codeManageFirstNumber
#                 codeInfo["codeName"] = getCodeByCodeNameObject.codeManageCodeName
#                 codeInfo["getReason"] = "根据程序第一次上传时间："+str(getCodeByCodeNameObject.codeManageUploadTime)
#                 codeInfoAll.append(codeInfo.copy())
#             # 根据标签的关键字  ===>  标签ID（全部标签名）  ===>  在主页里跳转到对应的标签上
#         getTagByTagNameObjects = codeManage.codeTag.objects.all().filter(codeTagName__icontains=keywords)
#         for getTagByTagNameObject in getTagByTagNameObjects:
#             tagInfo["tagID"] = getTagByTagNameObject.id
#             tagInfo["tagName"] = getTagByTagNameObject.codeTagName
#             tagInfo["getReason"] = "根据标签名："+getTagByTagNameObject.codeTagName
#             tagInfoAll.append(tagInfo.copy())
#
#         #iregex
#         #icontains
#         # keywords=".*".join(keywords)
#         if keywords[:4]=="reg:" and keywords[4:].strip()!="":
#             keywords=keywords[4:].strip()
#                 # 根据用户名的关键字  ===>  用户名（用户名）  ===>  用户主页
#             getUserByUserNameObjects = nomal_user.nomal_user.objects.all().filter(nomal_username__iregex=keywords)
#             for getUserByUserNameObject in getUserByUserNameObjects:
#                 userInfo["userID"] = getUserByUserNameObject.id
#                 userInfo["userName"] = getUserByUserNameObject.nomal_username
#                 userInfo["getReason"] = "正则用户名："+getUserByUserNameObject.nomal_username
#                 userInfoAll.append(userInfo.copy())
#                 # 根据学号的关键字  ===>  用户名（全部学号）  ===>  用户主页
#             getUserByUserNumberObjects = nomal_user.nomal_user.objects.all().filter(nomal_usernumber__iregex=keywords)
#             for getUserByUserNumberObject in getUserByUserNumberObjects:
#                 userInfo["userID"] = getUserByUserNumberObject.id
#                 userInfo["userName"] = getUserByUserNumberObject.nomal_username
#                 userInfo["getReason"] = "正则学号："+getUserByUserNumberObject.nomal_usernumber
#                 userInfoAll.append(userInfo.copy())
#                 # 根据年级班级的关键字  ===>  用户名（年级班级）  ===>  用户主页
#             getUserByUserGradeOrClassObjects = nomal_user.nomal_user.objects.all().filter(nomal_usergradeclass__iregex=keywords)
#             for getUserByUserGradeOrClassObject in getUserByUserGradeOrClassObjects:
#                 userInfo["userID"] = getUserByUserGradeOrClassObject.id
#                 userInfo["userName"] = getUserByUserGradeOrClassObject.nomal_username
#                 userInfo["getReason"] = "正则年级班级："+getUserByUserGradeOrClassObject.nomal_usergradeclass.split("_")[0]+"级"+getUserByUserGradeOrClassObject.nomal_usergradeclass.split("_")[1]+"班"
#                 userInfoAll.append(userInfo.copy())
#                 # 根据邮箱的关键字  ===>  用户名（全部邮箱）  ===>  用户主页
#             getUserByUserEmailObjects = nomal_user.nomal_user.objects.all().filter(nomal_useremail__iregex=keywords)
#             for getUserByUserEmailObject in getUserByUserEmailObjects:
#                 userInfo["userID"] = getUserByUserEmailObject.id
#                 userInfo["userName"] = getUserByUserEmailObject.nomal_username
#                 userInfo["getReason"] = "正则邮箱："+getUserByUserEmailObject.nomal_useremail
#                 userInfoAll.append(userInfo.copy())
#                 # 根据程序名字的关键字  ===>  程序名（全部程序名）  ===>  程序主页（仅显示工程）
#             getCodeByCodeNameObjects = codeManage.codeManage.objects.all().filter(codeManageIsDelete=False).filter(codeManageMainFlag=1).filter(codeManageCodeName__iregex=keywords)
#             for getCodeByCodeNameObject in getCodeByCodeNameObjects:
#                 codeInfo["codeFirstNumber"] = getCodeByCodeNameObject.codeManageFirstNumber
#                 codeInfo["codeName"] = getCodeByCodeNameObject.codeManageCodeName
#                 codeInfo["getReason"] = "正则程序名："+getCodeByCodeNameObject.codeManageCodeName
#                 codeInfoAll.append(codeInfo.copy())
#                 # 根据程序解释的关键字  ===>  程序名（全部解释）  ===>  程序主页（仅显示工程）
#             getCodeByCodeNameObjects = codeManage.codeManage.objects.all().filter(codeManageIsDelete=False).filter(codeManageCodeExplain__iregex=keywords)
#             for getCodeByCodeNameObject in getCodeByCodeNameObjects:
#                 codeInfo["codeFirstNumber"] = getCodeByCodeNameObject.codeManageFirstNumber
#                 codeInfo["codeName"] = getCodeByCodeNameObject.codeManageCodeName
#                 codeInfo["getReason"] = "正则程序说明："+getCodeByCodeNameObject.codeManageCodeExplain
#                 codeInfoAll.append(codeInfo.copy())
#                 # 根据程序提交的时间  ===>  程序名（全部提交时间）  ===>  程序主页（显示工程|！单独的程序版本）
#             if not check_contain_chinese(keywords):
#                 getCodeByCodeNameObjects = codeManage.codeManage.objects.all().filter(codeManageIsDelete=False).filter(codeManageMainFlag=1).filter(codeManageUploadTime__iregex=keywords)
#                 for getCodeByCodeNameObject in getCodeByCodeNameObjects:
#                     codeInfo["codeFirstNumber"] = getCodeByCodeNameObject.codeManageFirstNumber
#                     codeInfo["codeName"] = getCodeByCodeNameObject.codeManageCodeName
#                     codeInfo["getReason"] = "正则程序第一次上传时间："+str(getCodeByCodeNameObject.codeManageUploadTime)
#                     codeInfoAll.append(codeInfo.copy())
#                 # 根据标签的关键字  ===>  标签ID（全部标签名）  ===>  在主页里跳转到对应的标签上
#             getTagByTagNameObjects = codeManage.codeTag.objects.all().filter(codeTagName__iregex=keywords)
#             for getTagByTagNameObject in getTagByTagNameObjects:
#                 tagInfo["tagID"] = getTagByTagNameObject.id
#                 tagInfo["tagName"] = getTagByTagNameObject.codeTagName
#                 tagInfo["getReason"] = "正则标签名："+getTagByTagNameObject.codeTagName
#                 tagInfoAll.append(tagInfo.copy())
#
#         if keywords[:5]=="blur:" and keywords[5:].strip()!="":
#             keywords=".*".join(keywords[5:].strip())
#                 # 根据用户名的关键字  ===>  用户名（用户名）  ===>  用户主页
#             getUserByUserNameObjects = nomal_user.nomal_user.objects.all().filter(nomal_username__iregex=keywords)
#             for getUserByUserNameObject in getUserByUserNameObjects:
#                 userInfo["userID"] = getUserByUserNameObject.id
#                 userInfo["userName"] = getUserByUserNameObject.nomal_username
#                 userInfo["getReason"] = "模糊用户名："+getUserByUserNameObject.nomal_username
#                 userInfoAll.append(userInfo.copy())
#                 # 根据学号的关键字  ===>  用户名（全部学号）  ===>  用户主页
#             getUserByUserNumberObjects = nomal_user.nomal_user.objects.all().filter(nomal_usernumber__iregex=keywords)
#             for getUserByUserNumberObject in getUserByUserNumberObjects:
#                 userInfo["userID"] = getUserByUserNumberObject.id
#                 userInfo["userName"] = getUserByUserNumberObject.nomal_username
#                 userInfo["getReason"] = "模糊学号："+getUserByUserNumberObject.nomal_usernumber
#                 userInfoAll.append(userInfo.copy())
#                 # 根据年级班级的关键字  ===>  用户名（年级班级）  ===>  用户主页
#             getUserByUserGradeOrClassObjects = nomal_user.nomal_user.objects.all().filter(nomal_usergradeclass__iregex=keywords)
#             for getUserByUserGradeOrClassObject in getUserByUserGradeOrClassObjects:
#                 userInfo["userID"] = getUserByUserGradeOrClassObject.id
#                 userInfo["userName"] = getUserByUserGradeOrClassObject.nomal_username
#                 userInfo["getReason"] = "模糊年级班级："+getUserByUserGradeOrClassObject.nomal_usergradeclass.split("_")[0]+"级"+getUserByUserGradeOrClassObject.nomal_usergradeclass.split("_")[1]+"班"
#                 userInfoAll.append(userInfo.copy())
#                 # 根据邮箱的关键字  ===>  用户名（全部邮箱）  ===>  用户主页
#             getUserByUserEmailObjects = nomal_user.nomal_user.objects.all().filter(nomal_useremail__iregex=keywords)
#             for getUserByUserEmailObject in getUserByUserEmailObjects:
#                 userInfo["userID"] = getUserByUserEmailObject.id
#                 userInfo["userName"] = getUserByUserEmailObject.nomal_username
#                 userInfo["getReason"] = "模糊邮箱："+getUserByUserEmailObject.nomal_useremail
#                 userInfoAll.append(userInfo.copy())
#                 # 根据程序名字的关键字  ===>  程序名（全部程序名）  ===>  程序主页（仅显示工程）
#             getCodeByCodeNameObjects = codeManage.codeManage.objects.all().filter(codeManageIsDelete=False).filter(codeManageMainFlag=1).filter(codeManageCodeName__iregex=keywords)
#             for getCodeByCodeNameObject in getCodeByCodeNameObjects:
#                 codeInfo["codeFirstNumber"] = getCodeByCodeNameObject.codeManageFirstNumber
#                 codeInfo["codeName"] = getCodeByCodeNameObject.codeManageCodeName
#                 codeInfo["getReason"] = "模糊程序名："+getCodeByCodeNameObject.codeManageCodeName
#                 codeInfoAll.append(codeInfo.copy())
#                 # 根据程序解释的关键字  ===>  程序名（全部解释）  ===>  程序主页（仅显示工程）
#             getCodeByCodeNameObjects = codeManage.codeManage.objects.all().filter(codeManageIsDelete=False).filter(codeManageCodeExplain__iregex=keywords)
#             for getCodeByCodeNameObject in getCodeByCodeNameObjects:
#                 codeInfo["codeFirstNumber"] = getCodeByCodeNameObject.codeManageFirstNumber
#                 codeInfo["codeName"] = getCodeByCodeNameObject.codeManageCodeName
#                 codeInfo["getReason"] = "模糊程序说明："+getCodeByCodeNameObject.codeManageCodeExplain
#                 codeInfoAll.append(codeInfo.copy())
#                 # 根据程序提交的时间  ===>  程序名（全部提交时间）  ===>  程序主页（显示工程|！单独的程序版本）
#             if not check_contain_chinese(keywords):
#                 getCodeByCodeNameObjects = codeManage.codeManage.objects.all().filter(codeManageIsDelete=False).filter(codeManageMainFlag=1).filter(codeManageUploadTime__iregex=keywords)
#                 for getCodeByCodeNameObject in getCodeByCodeNameObjects:
#                     codeInfo["codeFirstNumber"] = getCodeByCodeNameObject.codeManageFirstNumber
#                     codeInfo["codeName"] = getCodeByCodeNameObject.codeManageCodeName
#                     codeInfo["getReason"] = "模糊程序第一次上传时间："+str(getCodeByCodeNameObject.codeManageUploadTime)
#                     codeInfoAll.append(codeInfo.copy())
#                 # 根据标签的关键字  ===>  标签ID（全部标签名）  ===>  在主页里跳转到对应的标签上
#             getTagByTagNameObjects = codeManage.codeTag.objects.all().filter(codeTagName__iregex=keywords)
#             for getTagByTagNameObject in getTagByTagNameObjects:
#                 tagInfo["tagID"] = getTagByTagNameObject.id
#                 tagInfo["tagName"] = getTagByTagNameObject.codeTagName
#                 tagInfo["getReason"] = "模糊标签名："+getTagByTagNameObject.codeTagName
#                 tagInfoAll.append(tagInfo.copy())
#         # print codeInfoAll
#         userInfoAll = sorted(userInfoAll,key=lambda e: e.__getitem__('userID'))
#         codeInfoAll = sorted(codeInfoAll,key=lambda e: e.__getitem__('codeFirstNumber'))
#     return  JsonResponse({"userInfoAll":userInfoAll,"codeInfoAll":codeInfoAll,"tagInfoAll":tagInfoAll},safe=False)
