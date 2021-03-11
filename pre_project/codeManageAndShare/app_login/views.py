# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth import authenticate, login, logout  #登入和登出
from django.contrib.auth.decorators import login_required  # 验证用户是否登录
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

@csrf_exempt
def app_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)  
        #user = authenticate(email=username,password=password)  
        #user = authenticate(username="shao",password="ning")  
        ## 类型为<class 'django.contrib.auth.models.User'>
        ## print(type(models.Customer.objects.get(name="赵凡")))
        ## print(user,type(user))
        print username+"  "+password
        print user
        if user:
            print username+"  "+password
            login(request,user)  # 验证成功之后登录
            return  HttpResponseRedirect('/selfPart')
    print "验证未成功"
    if str(request.user) != "AnonymousUser":
        print request.user
        print "已经登录进行重定向"
        return  HttpResponseRedirect('/selfPart')
    return render(request, "login.html")

def app_logout(request):
    logout(request)  # 登出
    return redirect("/login")
