# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

import os
import sys
import difflib
import random
import string
import datetime

import app_register.models as nomal_user
from models import codeManage
from models import codeTagRelation
from models import codeLanguage
from models import codeTag
from models import codeDiscuss
from app_selfPart.models import selfPartUserDynamic

# Create your views here.
# def codeManage_selfPartGetAllCode
@login_required
def codeManage_selfPartAddNewProjectGetIndex(request):
    # print request.user.first_name
    getAllLanguages = codeLanguage.objects.all()
    getAllCodeTags = codeTag.objects.all().order_by('-codeTagClickTimes')
    allLanguages = {}
    allCodeTags = {}
    for getAllLanguage in getAllLanguages:
        allLanguages[getAllLanguage.id] = getAllLanguage.codeLanguageType
    for getAllCodeTag in getAllCodeTags:
        allCodeTags[getAllCodeTag.id] = getAllCodeTag.codeTagName
    # print allLanguages
    return render(request,'codeManageAddNewProject.html',{'username':request.user.first_name,"allLanguages":allLanguages,"allCodeTags":allCodeTags})

@csrf_exempt
def codeManage_addOneCodeTag(request):
    if request.method == 'POST':
        aNewCodeTag = codeTag()
        aNewCodeTag.codeTagName = request.POST.get("codeTagName")
        aNewCodeTag.codeTagClickTimes = 0
        aNewCodeTag.codeTagLastClick = 0
        aNewCodeTag.save()
        currentCodeTagID = aNewCodeTag.id
        return JsonResponse(currentCodeTagID,safe=False)

@csrf_exempt
def codeManageUploadAjax(request):
    #这个函数的功能是上传一个新的项目
    if request.method == 'POST':
        currentUserID = int(nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id).id)
    	#下面是获取数据并写入数据库
        codeManageFirstNumber=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"_"+"".join(random.sample(string.ascii_letters + string.digits, 1))
        codeManageSecondNumber=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"_"+"".join(random.sample(string.ascii_letters + string.digits, 3))
        oneCodeWriteToDatabase = codeManage()
        oneCodeWriteToDatabase.codeManageMainFlag=1
        oneCodeWriteToDatabase.codeManageFirstNumber=codeManageFirstNumber
        oneCodeWriteToDatabase.codeManageSecondNumber=codeManageSecondNumber
    	oneCodeWriteToDatabase.codeManageCodeName = request.POST.get("codeProjectName")
        oneCodeWriteToDatabase.codeManageCodeAuthor = currentUserID
    	oneCodeWriteToDatabase.codeManageIsShare = request.POST.get("isShare")
    	oneCodeWriteToDatabase.codeManageLanguage = request.POST.get("languageChoice")
        oneCodeWriteToDatabase.codeManageSearchTimes = 0
        oneCodeWriteToDatabase.codeManageCheckTimes = 0
        oneCodeWriteToDatabase.codeManageDownloadTimes = 0
        oneCodeWriteToDatabase.codeManageCodeExplain = request.POST.get("codeExplain")
        oneCodeWriteToDatabase.save()

        #下面是建立标签与程序之间的联系
        currentCode = str(oneCodeWriteToDatabase.id)
        codeTagAll = request.POST.get("codeTag")
        if codeTagAll!="":
            codeTagAllList = codeTagAll.split(",")
            # print request.POST.get("codeTag")
            # print codeTagAll
            for codeTag in codeTagAllList:
                createNewTagRelation = codeTagRelation()
                createNewTagRelation.codeTagRelationiCodeID = currentCode
                createNewTagRelation.codeTagRelationTagID = codeTag
                createNewTagRelation.save()
                # print "codeTag: "+codeTag

        #下面是添加动态
        userDynamic = selfPartUserDynamic()
        userDynamic.selfPartUserDynamicUserID = currentUserID
        userDynamic.selfPartUserDynamicType = "data_addDate"
        userDynamic.selfPartUserDynamicPic = "xe690"
        userDynamic.selfPartUserDynamicCodeID = currentCode
        userDynamic.save()

        #下面是上传文件
    	BASE_DIR = os.path.abspath('.')+"/common_static/codeSavePosition/"+codeManageFirstNumber+"/"+codeManageSecondNumber
    	os.makedirs(BASE_DIR)
        file_obj = request.FILES.get('file')
        # BASE_DIR = '/root/python/django/codeManageAndShare/common_static/codeSavePosition'
        print BASE_DIR
        f = open(os.path.join(BASE_DIR, file_obj.name), 'wb')
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        oneCodeWriteToDatabase.codeManageSavePosition = "/static/codeSavePosition/"+codeManageFirstNumber+"/"+codeManageSecondNumber + "/" + file_obj.name
        oneCodeWriteToDatabase.save()
        return  HttpResponseRedirect('/selfPart')


# @login_required
def codeManage_selfPartOneProjectGetIndex(request):
    #这个函数的功能显示一个工程的主页面
    isLogin=0
    currentUserID = 0
    if request.user.is_authenticated():
        isLogin=1
        currentUserID = nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id).id
    getCodeManageFirstNumber = request.GET['codeManageFirstNumber']
    getAllCodes = codeManage.objects.all().filter(codeManageFirstNumber=getCodeManageFirstNumber,codeManageIsDelete=False) #.order_by("-codeManageUploadTime")
    codeMainInfo = {}
    codeOneInfo = {}
    codeOneInfos = []
    codeMainInfo["codename"] = getAllCodes[0].codeManageCodeName
    codeMainInfo["firstNumber"] = getAllCodes[0].codeManageFirstNumber
    for getAllCode in getAllCodes:
        # codeOneInfo["firstNumber"] = getAllCode.codeManageFirstNumber
        codeOneInfo["secondNumber"] = getAllCode.codeManageSecondNumber
        codeOneInfo["codeExplain"] = getAllCode.codeManageCodeExplain
        codeOneInfo["savePosition"] = getAllCode.codeManageSavePosition
        codeOneInfo["uploadTime"] = getAllCode.codeManageUploadTime
        codeOneInfos.append(codeOneInfo.copy())
    codeAuthorID = getAllCodes[0].codeManageCodeAuthor
    codeAuthorName = nomal_user.nomal_user.objects.get(id=codeAuthorID).nomal_username
    print codeAuthorName
    if isLogin==1 and int(codeAuthorID)==int(currentUserID):
        return render(request,'codeManageOneProject.html',{"codeMainInfo":codeMainInfo,"codeOneInfos":codeOneInfos,"isLogin":isLogin})
    elif isLogin==1 and int(codeAuthorID)!=int(currentUserID) and getAllCodes[0].codeManageIsShare==True:
        return render(request,'codeManageOneProjectOther.html',{"codeMainInfo":codeMainInfo,"codeOneInfos":codeOneInfos,"isLogin":isLogin,"codeAuthorID":codeAuthorID,"codeAuthorName":codeAuthorName})
    elif isLogin==1 and int(codeAuthorID)!=int(currentUserID) and getAllCodes[0].codeManageIsShare!=True:
        return render(request,'codeManageOneProjectForbidden.html',{"isLogin":isLogin})
    elif isLogin!=1 and getAllCodes[0].codeManageIsShare==True:
        return render(request,'codeManageOneProjectOther.html',{"codeMainInfo":codeMainInfo,"codeOneInfos":codeOneInfos,"isLogin":isLogin,"codeAuthorID":codeAuthorID,"codeAuthorName":codeAuthorName})
    elif isLogin!=1 and getAllCodes[0].codeManageIsShare!=True:
        return render(request,'codeManageOneProjectForbidden.html',{"isLogin":isLogin})
    else:
        return render(request,'codeManageOneProjectForbidden.html',{"isLogin":isLogin})

@csrf_exempt
def codeManage_getCodeCompare(request):
    #这个函数的功能是返回一个工程中的不同版本的修改信息
    # print selfPartAllCodeSimpleOnes
    # print selfPartAllCodeSimpleOnesPush
    getCodeManageSecondNumber = request.POST.get("thisSecondNumber")
    getCodeManageSecondNumberLast = request.POST.get("lastSecondNumber")
    # print "getCodeManageSecondNumber"+str(getCodeManageSecondNumber)
    getCodeManageThis = codeManage.objects.all().filter(codeManageSecondNumber=getCodeManageSecondNumber)[0]
    codeManageSavePosition = getCodeManageThis.codeManageSavePosition
    codeManageSavePositionLast = "common_"
    if getCodeManageSecondNumberLast != "":
        getCodeManageThisLast = codeManage.objects.all().filter(codeManageSecondNumber=getCodeManageSecondNumberLast)[0]
        codeManageSavePositionLast = codeManageSavePositionLast+getCodeManageThisLast.codeManageSavePosition[1:]
    # print "bash script/getCodeFileInfoUpGrade.sh common_"+codeManageSavePosition[1:]+" "+codeManageSavePositionLast
    getAllString = str(os.popen("bash script/getCodeFileInfoUpGrade.sh "+codeManageSavePositionLast+" common_"+codeManageSavePosition[1:]).read())
    # getAllString = str(os.popen("bash script/getCodeFileInfoUpGrade.sh common_"+codeManageSavePosition[1:]+" "+codeManageSavePositionLast).read())
    # print getAllString
    return JsonResponse(getAllString,safe=False)


def readfile(filename):
    #此函数的功能是读取文件
    try:
        fileHandle = open(filename,'r')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:' + str(error))
        sys.exit()

@csrf_exempt
def codeManage_getCodeCompare_ChangeDetil(request):
    textfile1 = request.POST.get("getCodeDifferentFileLast")
    textfile2 = request.POST.get("getCodeDifferentFileThis")
    text1_lines = readfile(textfile1)
    text2_lines = readfile(textfile2)
    d = difflib.HtmlDiff()
    # print(d.make_file(text1_lines,text2_lines))
    return JsonResponse(d.make_file(text1_lines,text2_lines),safe=False) #.replace('nowrap="nowrap"','style="width:100px;word-wrap:break-word;"')

# @login_required
# def codeManage_selfPartOneVersionGetIndex(request):
#     #这个函数的功能显示一个单独的版本
#     # getAllLanguages = codeLanguage.objects.all()
#     getCodeManageFirstNumber = request.GET['codeManageSecondNumber']  #"20180501224917_psQ" #
#     getCodeManageThis = codeManage.objects.all().filter(codeManageSecondNumber=getCodeManageFirstNumber)[0]
#     codeInfo={}
#     codeInfo["codename"] = getCodeManageThis.codeManageCodeName
#     codeInfo["uploadTime"] = str(getCodeManageThis.codeManageUploadTime)
#     codeInfo["codeExplain"] = getCodeManageThis.codeManageCodeExplain
#     codeManageSavePosition = getCodeManageThis.codeManageSavePosition
#     DIRNAME = "common_"+codeManageSavePosition[1:61]
#     getAllString = str(os.popen("bash script/getThisDirContentFileFirstStep.sh common_"+codeManageSavePosition[1:]).read())
#     print getAllString
#     getListDirs = getAllString.split("%%%")[1].split(",")
#     getListFiles = getAllString.split("%%%")[2][:-1].split(",")
#     codeTags={}
#     getAllCodeTagRelations = codeTagRelation.objects.all().filter(codeTagRelationiCodeID=getCodeManageThis.id)
#     for getAllCodeTagRelation in getAllCodeTagRelations:
#         getOneCodeTag = codeTag.objects.all().filter(id=getAllCodeTagRelation.codeTagRelationTagID)[0]
#         codeTags[getOneCodeTag.id] = getOneCodeTag.codeTagName
#     return render(request,'codeManageOneVersion.html',{'codeInfo':codeInfo,"codeTags":codeTags,"getListDirs":getListDirs,"getListFiles":getListFiles,"currentDir":getAllString.split("%%%")[0]})
#     # return render(request,'codeManageOneVersion.html',{'codeInfo':codeInfo})


# @login_required
def codeManage_selfPartOneVersionGetIndex(request):
    #这个函数的功能显示一个单独的版本
    # getAllLanguages = codeLanguage.objects.all()
    isLogin=0
    currentUserID = 0
    if request.user.is_authenticated():
        isLogin=1
        currentUserID = nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id).id
    getCodeManageSecondNumber = request.GET['codeManageSecondNumber']  #"20180501224917_psQ" #
    getCodeManageThis = codeManage.objects.all().filter(codeManageSecondNumber=getCodeManageSecondNumber)[0]
    getCodeManageThis.codeManageCheckTimes = str(int(getCodeManageThis.codeManageCheckTimes)+1)
    getCodeManageThis.save()
    codeInfo={}
    codeInfo["codename"] = getCodeManageThis.codeManageCodeName
    codeInfo["uploadTime"] = str(getCodeManageThis.codeManageUploadTime)
    codeInfo["codeExplain"] = getCodeManageThis.codeManageCodeExplain
    codeManageSavePosition = getCodeManageThis.codeManageSavePosition
    DIRNAME = "common_"+codeManageSavePosition[1:61]
    # print "DIRNAME:  " + DIRNAME
    getAllString = str(os.popen("bash script/getThisDirContentFileFirstStep.sh common_"+codeManageSavePosition[1:]+" "+DIRNAME).read())
    # print getAllString
    getListDirs = getAllString.split("%%%")[1].split(",")
    getListFiles = getAllString.split("%%%")[2][:-1].split(",")
    codeTags={}
    codeMainSecondID = codeManage.objects.all().filter(codeManageFirstNumber=getCodeManageThis.codeManageFirstNumber)[0].id
    getAllCodeTagRelations = codeTagRelation.objects.all().filter(codeTagRelationiCodeID=codeMainSecondID)
    for getAllCodeTagRelation in getAllCodeTagRelations:
        getOneCodeTag = codeTag.objects.all().filter(id=getAllCodeTagRelation.codeTagRelationTagID)[0]
        codeTags[getOneCodeTag.id] = getOneCodeTag.codeTagName
    codeAuthorID = getCodeManageThis.codeManageCodeAuthor
    codeAuthorName = nomal_user.nomal_user.objects.get(id=codeAuthorID).nomal_username
    print codeAuthorName
    if getCodeManageThis.codeManageIsDelete==True:
        return render(request,'codeManageOneVersionNotExist.html',{"isLogin":isLogin})
    else:
        if isLogin==1 and int(codeAuthorID)==int(currentUserID):
            return render(request,'codeManageOneVersion.html',{'codeInfo':codeInfo,"codeTags":codeTags,"getListDirs":getListDirs,"getListFiles":getListFiles,"currentDir":getAllString.split("%%%")[0],"isLogin":isLogin})
        elif isLogin==1 and int(codeAuthorID)!=int(currentUserID) and getCodeManageThis.codeManageIsShare==True:
            return render(request,'codeManageOneVersionOther.html',{'codeInfo':codeInfo,"codeTags":codeTags,"getListDirs":getListDirs,"getListFiles":getListFiles,"currentDir":getAllString.split("%%%")[0],"isLogin":isLogin,"codeAuthorID":codeAuthorID,"codeAuthorName":codeAuthorName})
        elif isLogin==1 and int(codeAuthorID)!=int(currentUserID) and getCodeManageThis.codeManageIsShare!=True:
            return render(request,'codeManageOneProjectForbidden.html',{"isLogin":isLogin})
        elif isLogin!=1 and getCodeManageThis.codeManageIsShare==True:
            return render(request,'codeManageOneVersionOther.html',{'codeInfo':codeInfo,"codeTags":codeTags,"getListDirs":getListDirs,"getListFiles":getListFiles,"currentDir":getAllString.split("%%%")[0],"isLogin":isLogin,"codeAuthorID":codeAuthorID,"codeAuthorName":codeAuthorName})
        elif isLogin!=1 and getCodeManageThis.codeManageIsShare!=True:
            return render(request,'codeManageOneProjectForbidden.html',{"isLogin":isLogin})
        else:
            return render(request,'codeManageOneProjectForbidden.html',{"isLogin":isLogin})
    # return render(request,'codeManageOneVersion.html',{'codeInfo':codeInfo})

@csrf_exempt
def codeManage_selfPartOneVersionGetIndex_returnPath(request):
    #这个函数的功能是通过AJAX返回一个单独的版本的目录结构  
    # print "getCurrentDirPath"+str(request.POST.get("currentDirPath").replace('\t','').replace('\n','').replace(' ',''))
    # print request.POST.get("clickDirName")
    # print request.POST.get("currentCodeSecondNumber")
    getThisCodeSavePosition = codeManage.objects.all().filter(codeManageSecondNumber=request.POST.get("currentCodeSecondNumber"))[0].codeManageSavePosition
    getCurrentDirPath = str(request.POST.get("currentDirPath").replace('\t','').replace('\n','').replace(' ',''))
    getThisTimeWorkPath = getThisCodeSavePosition[:61]+"temp/"+getCurrentDirPath+request.POST.get("clickDirName")
    # print getThisTimeWorkPath
    getAllString = str(os.popen("bash script/getThisDirContentFile.sh common_"+getThisTimeWorkPath[1:]).read())
    # print getAllString
    getListDirs = getAllString.split("###")[0].split(",")
    getListFiles = getAllString.split("###")[1][:-1].split(",")
    returnPathContent = {"getListDirs":getListDirs,"getListFiles":getListFiles,"currentDir":request.POST.get("clickDirName"),"currentAllPath":getCurrentDirPath}
    # print returnPathContent
    return JsonResponse(returnPathContent,safe=False)

@login_required
def codeManage_selfPartAddNewVersionGetIndex(request):
    #这个函数的功能是上传不同版本的主页
    getCodeManageFirstNumber = request.GET['codeManageFirstNumber']
    getCodeManageThis = codeManage.objects.all().filter(codeManageFirstNumber=getCodeManageFirstNumber)[0]
    codeInfo = {}
    codeInfo["codeName"] = getCodeManageThis.codeManageCodeName
    codeInfo["codeLanguageID"] = getCodeManageThis.codeManageLanguage
    codeInfo["codeLanguage"] = codeLanguage.objects.all().filter(id=getCodeManageThis.codeManageLanguage)[0].codeLanguageType
    codeInfo["codeIsshareCode"] = getCodeManageThis.codeManageIsShare
    if getCodeManageThis.codeManageIsShare:
        codeInfo["codeIsshare"] = "公开"
    else:
        codeInfo["codeIsshare"] = "不公开"
    # print codeInfo
    return render(request,'codeManageAddNewVersion.html',{'username':request.user.first_name,"codeInfo":codeInfo})


@csrf_exempt
def codeManageUploadAjaxNewVersion(request):
    #这个函数的功能是上传不同版本的程序
    if request.method == 'POST':
        currentUserID = int(nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id).id)
        #下面是获取数据并写入数据库
        codeManageFirstNumber=request.POST.get("codeFirstNumber")
        codeManageSecondNumber=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"_"+"".join(random.sample(string.ascii_letters + string.digits, 3))
        oneCodeWriteToDatabase = codeManage()
        oneCodeWriteToDatabase.codeManageMainFlag=0
        oneCodeWriteToDatabase.codeManageFirstNumber=codeManageFirstNumber
        oneCodeWriteToDatabase.codeManageSecondNumber=codeManageSecondNumber
        oneCodeWriteToDatabase.codeManageCodeName = request.POST.get("codeProjectName")
        oneCodeWriteToDatabase.codeManageCodeAuthor = currentUserID
        oneCodeWriteToDatabase.codeManageIsShare = request.POST.get("isShare")
        oneCodeWriteToDatabase.codeManageLanguage = request.POST.get("languageChoice")
        oneCodeWriteToDatabase.codeManageSearchTimes = 0
        oneCodeWriteToDatabase.codeManageCheckTimes = 0
        oneCodeWriteToDatabase.codeManageDownloadTimes = 0
        oneCodeWriteToDatabase.codeManageCodeExplain = request.POST.get("codeExplain")
        oneCodeWriteToDatabase.save()
        #添加版本不需要添加标签 #下面是建立标签与程序之间的联系
        currentCode = str(oneCodeWriteToDatabase.id)
        # codeTagAll = request.POST.get("codeTag").split(",")
        # for codeTag in codeTagAll:
        #     createNewTagRelation = codeTagRelation()
        #     createNewTagRelation.codeTagRelationiCodeID = currentCode
        #     createNewTagRelation.codeTagRelationTagID = codeTag
        #     createNewTagRelation.save()
        #     # print "codeTag: "+codeTag

        #下面是添加动态
        userDynamic = selfPartUserDynamic()
        userDynamic.selfPartUserDynamicUserID = currentUserID
        userDynamic.selfPartUserDynamicType = "data_update"
        userDynamic.selfPartUserDynamicPic = "xe665"
        userDynamic.selfPartUserDynamicCodeID = currentCode
        userDynamic.save()

        #下面是上传文件
        BASE_DIR = os.path.abspath('.')+"/common_static/codeSavePosition/"+codeManageFirstNumber+"/"+codeManageSecondNumber
        os.makedirs(BASE_DIR)
        file_obj = request.FILES.get('file')
        # BASE_DIR = '/root/python/django/codeManageAndShare/common_static/codeSavePosition'
        print BASE_DIR
        f = open(os.path.join(BASE_DIR, file_obj.name), 'wb')
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        oneCodeWriteToDatabase.codeManageSavePosition = "/static/codeSavePosition/"+codeManageFirstNumber+"/"+codeManageSecondNumber + "/" + file_obj.name
        oneCodeWriteToDatabase.save()
        return  HttpResponseRedirect('/selfPart')









#下面是未登录的
def codeManage_allPartCodeSelectAndShow(request):
    # 这个函数的功能是代码库的部分，根据分类来进行检索
    getAllLanguages = codeLanguage.objects.all()
    getAllCodeTags = codeTag.objects.all().order_by('-codeTagClickTimes')
    allLanguages = {}
    allCodeTags = {}
    for getAllLanguage in getAllLanguages:
        allLanguages[getAllLanguage.id] = getAllLanguage.codeLanguageType
    for getAllCodeTag in getAllCodeTags:
        allCodeTags[getAllCodeTag.id] = getAllCodeTag.codeTagName
    return render(request,'codeSelectAndShow.html',{"allLanguages":allLanguages,"allCodeTags":allCodeTags})

@csrf_exempt
def codeManage_allPartCodeSelectAndShowAjaxGetCode(request):
    # 这个函数的功能是代码库的部分，根据条件获取代码
    if request.method == 'POST':
        getOption_language = request.POST.get("language")
        getOption_codeTag = request.POST.get("codeTag")
        getCodeAll = codeManage.objects.all().filter(codeManageIsDelete=False)
        getPushCodeAll = []
        getPushCodeOne = {}
        getPushCodeOneTag = {}
        if getOption_language != "0" and getOption_codeTag == "0":
            getCodeAll = getCodeAll.filter(codeManageMainFlag=1).filter(codeManageLanguage=getOption_language)
        if getOption_language == "0" and getOption_codeTag != "0":
            thisClickTagObject = codeTag.objects.all().filter(id=getOption_codeTag)[0]
            thisClickTagObject.codeTagClickTimes = int(thisClickTagObject.codeTagClickTimes)+1
            thisClickTagObject.save()
            getCodeAllFOrOnlyTag = getCodeAll.filter(id=0)
            for getCodeTagRelation in codeTagRelation.objects.all().filter(codeTagRelationTagID=getOption_codeTag):
                getCodeAllFOrOnlyTag = getCodeAllFOrOnlyTag | getCodeAll.filter(id=getCodeTagRelation.codeTagRelationiCodeID)
            getCodeAll = getCodeAllFOrOnlyTag.filter(codeManageMainFlag=1)
        if getOption_language != "0" and getOption_codeTag != "0":
            getCodeAllFOrOnlyTag = getCodeAll.filter(id=0)
            for getCodeTagRelation in codeTagRelation.objects.all().filter(codeTagRelationTagID=getOption_codeTag):
                getCodeAllFOrOnlyTag = getCodeAllFOrOnlyTag | getCodeAll.filter(id=getCodeTagRelation.codeTagRelationiCodeID)
            getCodeAll = getCodeAllFOrOnlyTag.filter(codeManageMainFlag=1).filter(codeManageLanguage=getOption_language)
        getCodeAll = getCodeAll.filter(codeManageMainFlag=1).order_by('-codeManageCheckTimes')
        for getCodeOne in getCodeAll:
            getPushCodeOne["codeName"] = getCodeOne.codeManageCodeName
            getPushCodeOne["codeFirstNumber"] = getCodeOne.codeManageFirstNumber
            getPushCodeOne["codeAuthorID"] = getCodeOne.codeManageCodeAuthor
            getPushCodeOne["codeAuthorName"] =  nomal_user.nomal_user.objects.get(id=getCodeOne.codeManageCodeAuthor).nomal_username
            getPushCodeOne["codeLanguage"] =  codeLanguage.objects.all().filter(id=getCodeOne.codeManageLanguage)[0].codeLanguageType
            getPushCodeOne["codeExplain"] =  getCodeOne.codeManageCodeExplain
            for getCodeTag in codeTagRelation.objects.all().filter(codeTagRelationiCodeID=getCodeOne.id):
                getPushCodeOneTagOne = codeTag.objects.all().filter(id=getCodeTag.codeTagRelationTagID)[0]
                getPushCodeOneTag[getPushCodeOneTagOne.id] = getPushCodeOneTagOne.codeTagName
            getPushCodeOne["codeTags"] = getPushCodeOneTag.copy()
            getPushCodeAll.append(getPushCodeOne.copy())
    return JsonResponse(getPushCodeAll,safe=False)



def main_showIndex(request):
    # 这个函数的功能是显示主页
    isLogin=0
    if request.user.is_authenticated():
        isLogin=1
    return render(request,'index.html',{"isLogin":isLogin})

def main_showIndex_getHotTag(request):
    getTagCount = int(codeTag.objects.all().count()/5)
    if getTagCount<10:
        getTagCount=10
    getAllHotTags = codeTag.objects.all().order_by("-codeTagClickTimes")[:getTagCount]
    getPushHotTagToIndex={}
    for getAllHotTag in getAllHotTags:
        getPushHotTagToIndex[getAllHotTag.id] = getAllHotTag.codeTagName
    # print getPushHotTagToIndex
    return JsonResponse(getPushHotTagToIndex,safe=False)


@csrf_exempt
def codeManage_oneCodeFileShow(request):
    # 这个函数的功能是在显示单个版本的部分，根据点击的代码文件返回相应的代码并进行展示
    getCodeSecondNumber = request.POST.get("cdoeFileSecondNumber").strip().replace('\t','').replace('\n','').replace(' ','')
    getCodeDirPath = request.POST.get("cdoeFilePath").strip().replace('\t','').replace('\n','').replace(' ','')
    getCodeFileName = request.POST.get("cdoeFileName").strip().replace('\t','').replace('\n','').replace(' ','')
    # print getCodeSecondNumber
    # print getCodeDirPath
    # print getCodeFileName
    codeSavePositonSketchy = codeManage.objects.all().filter(codeManageSecondNumber=getCodeSecondNumber)[0].codeManageSavePosition[:61]
    codeSavePositon = "common_"+codeSavePositonSketchy[1:]+"temp/"+getCodeDirPath+getCodeFileName
    print codeSavePositon
    
    codeType = "nodefined"
    codeNamePostfix = getCodeFileName.split('.')[-1]
    if codeNamePostfix == "html":
        codeType = "html"
    elif codeNamePostfix == "java":
        codeType = "java"
    elif codeNamePostfix == "cpp":
        codeType = "c_cpp"
    elif codeNamePostfix == "css":
        codeType = "css"
    elif codeNamePostfix == "sh":
        codeType = "sh"
    elif codeNamePostfix == "py":
        codeType = "python"
    elif codeNamePostfix == "php":
        codeType = "php"
    elif codeNamePostfix == "sql":
        codeType = "mysql"
    elif codeNamePostfix == "js":
        codeType = "javascript"
    elif codeNamePostfix == "json":
        codeType = "json"
    elif codeNamePostfix == "jsp":
        codeType = "jsp"
    # print "codeType::"+codeType

    getCodeAllString = ""
    # print str(os.popen("file -b "+codeSavePositon).read())
    thisFileTypeList = str(os.popen("file -b "+codeSavePositon).read())[:-1].replace(',',' ').split(" ")
    print thisFileTypeList
    print "text" in thisFileTypeList
    if "text" in thisFileTypeList:
        with open(codeSavePositon, 'r') as codeFile:
            getCodeAllString = codeFile.read()
        return render(request,'codeShowPart.html',{"getCodeAllString":getCodeAllString,"codeType":codeType})
    else:
        print '/'+codeSavePositon[7:]
        return JsonResponse({"file":'/'+codeSavePositon[7:]},safe=False)



@csrf_exempt
def codeManage_oneCodeFileShowForProjectShow(request):
    # 这个函数的功能是在显示单个工程的部分，根据点击的代码文件返回相应的代码并进行展示
    codeSavePositon = request.POST.get("codeAllPath").strip().replace('\t','').replace('\n','').replace(' ','')

    print codeSavePositon
    codeType = "nodefined"
    codeNamePostfix = codeSavePositon.split('.')[-1]
    if codeNamePostfix == "html":
        codeType = "html"
    elif codeNamePostfix == "java":
        codeType = "java"
    elif codeNamePostfix == "cpp":
        codeType = "c_cpp"
    elif codeNamePostfix == "css":
        codeType = "css"
    elif codeNamePostfix == "sh":
        codeType = "sh"
    elif codeNamePostfix == "py":
        codeType = "python"
    elif codeNamePostfix == "php":
        codeType = "php"
    elif codeNamePostfix == "sql":
        codeType = "mysql"
    elif codeNamePostfix == "js":
        codeType = "javascript"
    elif codeNamePostfix == "json":
        codeType = "json"
    elif codeNamePostfix == "jsp":
        codeType = "jsp"
    # print "codeType::"+codeType

    getCodeAllString = ""
    # print str(os.popen("file -b "+codeSavePositon).read())
    thisFileTypeList = str(os.popen("file -b "+codeSavePositon).read())[:-1].replace(',',' ').split(" ")
    print thisFileTypeList
    print "text" in thisFileTypeList
    if "text" in thisFileTypeList:
        with open(codeSavePositon, 'r') as codeFile:
            getCodeAllString = codeFile.read()
        return render(request,'codeShowPart.html',{"getCodeAllString":getCodeAllString,"codeType":codeType})
    else:
        print '/'+codeSavePositon[7:]
        return JsonResponse({"file":'/'+codeSavePositon[7:]},safe=False)




@csrf_exempt
def codeManage_deleteOneVersion(request):
    thisVersionSecondNumber = request.POST.get("secondNumber")
    # print thisVersionSecondNumber
    thisVersionAuthorID = codeManage.objects.all().filter(codeManageSecondNumber=thisVersionSecondNumber)[0].codeManageCodeAuthor #获取作者ID
    thisVersionID = codeManage.objects.all().filter(codeManageSecondNumber=thisVersionSecondNumber)[0].id
    #将此程序状态置为删除
    thisVersionObjects = codeManage.objects.all().filter(id=thisVersionID)[0]
    thisVersionObjects.codeManageIsDelete=1
    thisVersionObjects.save()
    #添加删除动态
    addDelDynamic = selfPartUserDynamic()
    addDelDynamic.selfPartUserDynamicUserID = thisVersionAuthorID
    addDelDynamic.selfPartUserDynamicType = "data_delDate"
    addDelDynamic.selfPartUserDynamicPic = "xe663"
    addDelDynamic.selfPartUserDynamicCodeID = thisVersionID
    addDelDynamic.save()
    return JsonResponse("删除成功",safe=False)


@csrf_exempt
def codeManage_getAllDiscuss(request):
    #这个函数的功能是根据程序的版本号返回所有的评论
    getAllDiscuss = []
    getOneDiscuss = {}
    getCodeSecondNumber = request.POST.get("codeSecondNumber")
    if request.user.is_authenticated():
        getCurrentLoginUserID = int(nomal_user.nomal_user.objects.get(nomal_userconfirmid=request.user.id).id)
    else:
        getCurrentLoginUserID = 0
    getALlDiscussObjects = codeDiscuss.objects.all().filter(codeDiscussSecondNumber=getCodeSecondNumber,codeDiscussIsDelete=False)
    for getALlDiscussObject in getALlDiscussObjects:
        getOneDiscuss["CreateID"] = getALlDiscussObject.codeDiscussUserCreateID
        getOneDiscuss["CreateName"] = nomal_user.nomal_user.objects.get(id=getALlDiscussObject.codeDiscussUserCreateID).nomal_username
        getOneDiscuss["CreateImg"] = nomal_user.nomal_user.objects.get(id=getALlDiscussObject.codeDiscussUserCreateID).nomal_userImg
        getOneDiscuss["ReplyID"] = getALlDiscussObject.codeDiscussUserReplyID
        if getALlDiscussObject.codeDiscussUserReplyID != "0":
            getOneDiscuss["ReplyName"] = nomal_user.nomal_user.objects.get(id=getALlDiscussObject.codeDiscussUserReplyID).nomal_username
        else:
            getOneDiscuss["ReplyName"] = ""
        getOneDiscuss["CreateDataTime"] = str(getALlDiscussObject.codeDiscussCreateDataTime)
        getOneDiscuss["Content"] = getALlDiscussObject.codeDiscussContent
        getAllDiscuss.append(getOneDiscuss.copy())
    # print getCodeSecondNumber
    return JsonResponse({"getCurrentLoginUserID":getCurrentLoginUserID,"getAllDiscuss":getAllDiscuss},safe=False)

@csrf_exempt
def codeManage_getAllDiscussForWriteToDB(request):
    #这个函数的功能是将AjAx传来的评论写入数据库
    if not request.user.is_authenticated():
        return JsonResponse("noLogin",safe=False)
    discussCreateID = request.POST.get("discussCreateID")
    discussReplyID = request.POST.get("discussReplyID")
    discussSecondNumber = request.POST.get("discussSecondNumber")
    DiscussContent = request.POST.get("oneDiscussContent")
    createObjecctForWriteDiscuss = codeDiscuss()
    createObjecctForWriteDiscuss.codeDiscussSecondNumber = discussSecondNumber
    createObjecctForWriteDiscuss.codeDiscussUserCreateID = discussCreateID
    createObjecctForWriteDiscuss.codeDiscussUserReplyID = discussReplyID
    createObjecctForWriteDiscuss.codeDiscussIsDelete = False
    createObjecctForWriteDiscuss.codeDiscussContent = DiscussContent
    createObjecctForWriteDiscuss.save()
    return JsonResponse("ok",safe=False)

@csrf_exempt
def codeManage_getNewestDiscuss(request):
    newestDiscussAll=[]
    newestDiscussOne={}
    getNewestDiscussObjects = codeDiscuss.objects.all().order_by('-codeDiscussCreateDataTime')[:10]
    for getNewestDiscussObject in getNewestDiscussObjects:
        newestDiscussOne["codeSecondNumber"] = getNewestDiscussObject.codeDiscussSecondNumber
        newestDiscussOne["userName"] = nomal_user.nomal_user.objects.get(id=getNewestDiscussObject.codeDiscussUserCreateID).nomal_username
        newestDiscussOne["discussContent"] = getNewestDiscussObject.codeDiscussContent
        newestDiscussAll.append(newestDiscussOne.copy())
    return JsonResponse(newestDiscussAll,safe=False)

@csrf_exempt
def codeManage_getHotestCode(request):
    hotestCOdeAll=[]
    hotestCOdeOne={}
    getHotestCodeObjects = codeManage.objects.all().filter(codeManageIsDelete=False).order_by('-codeManageCheckTimes')[:10]
    for getHotestCodeObject in getHotestCodeObjects:
        hotestCOdeOne["codeSecondNumber"] = getHotestCodeObject.codeManageSecondNumber
        hotestCOdeOne["codeName"] = getHotestCodeObject.codeManageCodeName
        hotestCOdeOne["codeExplain"] = getHotestCodeObject.codeManageCodeExplain
        hotestCOdeOne["codeCheckTimes"] = getHotestCodeObject.codeManageCheckTimes
        hotestCOdeAll.append(hotestCOdeOne.copy())
    return JsonResponse(hotestCOdeAll,safe=False)