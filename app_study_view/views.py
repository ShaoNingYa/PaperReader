# coding: utf-8
import time
import json
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app_study_view import models
from app_user_manage.models import UserToken
from app_user_manage.models import UserProfile


# Create your views here.


def index(request):
    return HttpResponse("学习管理的主页")


@csrf_exempt
def todolist_get_today(request):
    """获取所有的今日待办
    :param request:
    :return:
    """
    todolist_today = []
    is_complete = [False, True]
    data_get = models.ToDoList.objects.all().filter(
        sub_user=UserToken.objects.all().filter(user_token=request.POST.get("token"), is_alive=0)[0].username)
    for data_one in data_get:
        todo_one = {
            "text": str(data_one.content),
            "done": is_complete[data_one.is_complete]
        }
        todolist_today.append(todo_one.copy())
    return HttpResponse(json.dumps({"code": 20000, "date": time.strftime("%Y-%m-%d"), "data": todolist_today}))


@csrf_exempt
def todolist_update_today(request):
    """对今日待办进行更新
    :param request:
    :return:
    """
    data_get = request.POST.get("token")  # 从前端获取TODOList
    user_token = request.POST.get("token")
    username = UserToken.objects.all().filter(user_token=user_token, is_alive=0)[0].username
    data_get_from_db = models.ToDoList.objects.all().filter(sub_user=username)  # 获取数据库中当前用户的TODOList
    obj = data_get_from_db.filter(valid_time=date.today())
    return HttpResponse(json.dumps({"code": 20000, "date": time.strftime("%Y-%m-%d"), "data": str(len(obj)) + str([i.content for i in obj])}))
