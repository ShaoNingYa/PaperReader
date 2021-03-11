# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from models import nomal_user

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User

import random
import string
import os

# Create your views here.
def app_register(request):
    return render(request,'index_register.html')
def ajax_sendEmail(request):
    confirmEmail=request.GET['conFirmEmail']
    all =nomal_user.objects.all()
    if len(all.filter(nomal_useremail=confirmEmail)) == 0:
        confirmCode=''.join(random.sample(string.ascii_letters + string.digits, 6))
        nomal_user.objects.create(nomal_useremail=confirmEmail,nomal_useremailconfirm=confirmCode)
        os.system('bash app_register/sendEmail.sh '+confirmCode+' '+confirmEmail)
        state="发送成功"
        print "一个新邮箱"
    elif all.filter(nomal_useremail=confirmEmail)[0].nomal_useremailconfirm != "ok":
        confirmCode=''.join(random.sample(string.ascii_letters + string.digits, 6))
        nomal_user.objects.get(nomal_useremail=request.POST.get("regEmail")).nomal_useremailconfirm = confirmCode
        nomal_user.objects.get(nomal_useremail=request.POST.get("regEmail")).save()
        os.system('bash app_register/sendEmail.sh '+confirmCode+' '+confirmEmail)
        state="发送成功"
        print "一个旧邮箱"
    else:
        state = "已被注册"
    return JsonResponse(state,safe=False)

@csrf_exempt
def app_register_infowrite(request):
    if request.method == "POST":
        regUpdateGet=nomal_user.objects.get(nomal_useremail=request.POST.get("regEmail"))
        if request.POST.get("regConfirm") == regUpdateGet.nomal_useremailconfirm:
            print "邮箱验证码验证成功"
            #user = User.objects.create_user(request.POST.get("regTrueName"), request.POST.get("regEmail"), request.POST.get("regPassword"))
            user = User.objects.create_user(request.POST.get("regStudyNumber"),request.POST.get("regEmail"),request.POST.get("regPassword"))
            #user.password=request.POST.get("regPassword")
            user.is_superuser=0
            #user.username=request.POST.get("regStudyNumber")
            user.first_name=request.POST.get("regTrueName")
            #user.email=request.POST.get("regEmail")
            user.save()
            print "用户创建成功"
            regUpdateGet.nomal_username = request.POST.get("regTrueName")
            regUpdateGet.nomal_usersex = request.POST.get("sexChoice")
            regUpdateGet.nomal_usergradeclass = request.POST.get("gradeChoice")+"_"+request.POST.get("classChoice")
            regUpdateGet.nomal_usernumber = request.POST.get("regStudyNumber")
            #regUpdateGet.nomal_userpassword = request.POST.get("regPassword")
            #nomal_useremail = request.POST.get("regEmail")
            regUpdateGet.nomal_useremailconfirm = "ok"#request.POST.get("regConfirm")
            regUpdateGet.nomal_userconfirmid = str(user.id)
            regUpdateGet.nomal_userImg="/static/selfPart/userImg/default.png"
            regUpdateGet.save()
            print "完整数据写入成功"
            return  redirect('/login')
        else:
            print "邮箱验证码验证失败"
    return JsonResponse("失败",safe=False)
    #return render(request, "/login/")
