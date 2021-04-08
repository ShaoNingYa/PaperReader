import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from app_user_manage.models import UserToken
from rest_framework_jwt.utils import jwt_decode_handler


# Create your views here.
def index(request):
    return HttpResponse("用户管理的主页")


@csrf_exempt
def login(request):  # 根据用户和密码获取token
    def valid_password(_user):
        """验证成功，返回对应的身份，否则返回none"""
        # print("获取Token", default_token_generator.make_token(_user))  # 5o3-53ae30d9ccc25d0404f7
        # print("验证Token", default_token_generator.check_token(_user, "5o3-53ae30d9ccc25d0404f3"))
        # print(_user.pk, type(_user))
        # TODO 存储到令牌表中，取出的过程要更改，比如is_alive 要进行判断，除了0还有之外的可能
        token_get = UserToken.objects.all().filter(username=_user, is_alive=0)
        if token_get:  # 如果令牌表里有令牌，且可用，就将其取出，并返回
            return {"token": token_get[0].user_token}
        else:  # 否则重新生成，并保存到表中
            _token = default_token_generator.make_token(_user)
            UserToken.objects.create(username=_user, user_token=_token)
            return {"token": _token}

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return HttpResponse(json.dumps({"code": 20000, "data": valid_password(user)}))
    return HttpResponse(json.dumps({"code": 60204, "data": 'Account and password are incorrect.'}))


def info(request):  # 根据token查用户
    if request.method == 'GET':
        user_token = request.GET["token"]
        token_obj = UserToken.objects.all().filter(user_token=user_token, is_alive=0)
        if token_obj:
            user_data = {
                "roles": ["admin"],
                "avatar": str(token_obj[0].username.image),
                "name": token_obj[0].username.nick_name
            }
            return HttpResponse(json.dumps({"code": 20000, "data": user_data}))
    return HttpResponse(json.dumps({"code": 50008, "data": 'Login failed, unable to get user details.'}))


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        print("user logout")
    return HttpResponse(json.dumps({"code": 20000, "data": 'success'}))
