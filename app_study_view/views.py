# coding: utf-8
import time
import json
import logging
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app_study_view import models
from app_user_manage.models import UserToken
from app_user_manage.models import UserProfile

logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)
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
    data_get = data_get.filter(valid_time=date.today())
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
    data_get = request.POST.get("data").rstrip("{end}")  # 从前端获取TODOList
    user_token = request.POST.get("token")
    username = UserToken.objects.all().filter(user_token=user_token, is_alive=0)[0].username
    models.ToDoListLog.objects.create(  # 创建新的ToDoList放到数据库中
        sub_user=username,
        content=data_get,
    )
    data_get_from_db = models.ToDoList.objects.all().filter(sub_user=username)  # 获取数据库中当前用户的TODOList
    obj = data_get_from_db.filter(valid_time=date.today())  # 找到今天的
    obj.delete()  # 将所有今天的删掉
    for data_one_str in data_get.split("{end}"):
        if not data_one_str:
            continue
        text, done = data_one_str.strip().split(", ")
        done = True if done == "true" else False
        models.ToDoList.objects.create(  # 创建新的ToDoList放到数据库中
            sub_user=username,
            content=text,
            is_complete=done,
        )
    return HttpResponse(json.dumps({"code": 20000, "data": "success"}))


@csrf_exempt
def todolist_get_history(request):
    """获取所有的今日待办
    :param request:
    :return:
    """
    todolist_history = []
    temp_save = {}
    user_token = request.POST.get("token")
    username = UserToken.objects.all().filter(user_token=user_token, is_alive=0)[0].username
    is_complete = [False, True]
    data_get = models.ToDoList.objects.all().filter(sub_user=username)
    data_get = data_get.exclude(valid_time=date.today())
    for data_one in data_get:
        todo_one = {
            "text": str(data_one.content),
            "done": is_complete[data_one.is_complete]
        }
        cur_time = str(data_one.valid_time)
        cur_list = temp_save.get(cur_time, [])
        cur_list.append(todo_one.copy())
        temp_save[cur_time] = cur_list
    print(temp_save)
    todolist_history = [{"date": data_one_day[0], "data": data_one_day[1]} for data_one_day in temp_save.items()][::-1]
    return HttpResponse(json.dumps({"code": 20000, "data": todolist_history}))


@csrf_exempt
def todolist_get_template(request):
    """获取所有的今日待办
    :param request:
    :return:
    """
    user_token = request.POST.get("token")
    username = UserToken.objects.all().filter(user_token=user_token, is_alive=0)[0].username
    template_obj_all = models.TemplateForTODOmanage.objects.all().filter(sub_user=username)
    if not template_obj_all:
        return HttpResponse(json.dumps({"code": 20000, "data": []}))
    return_res = []
    for template_obj_one in template_obj_all:
        # print(template_obj_one.name)
        template_items_obj_all = models.ToDoListTemplate.objects.all().filter(sub_template=template_obj_one)
        temp_save = []
        for template_items_obj_one in template_items_obj_all:
            # print(template_items_obj_one.content)
            todo_one = {
                "text": str(template_items_obj_one.content),
                "done": False
            }
            temp_save.append(todo_one)
        template_one = {
            "title": template_obj_one.name,
            "data": temp_save
        }
        return_res.append(template_one)
    # print(return_res)
    return HttpResponse(json.dumps({"code": 20000, "data": return_res}))


@csrf_exempt
def todolist_update_template(request):
    """对模板进行更新
    :param request:
    :return:
    """
    data_get = request.POST.get("data").rstrip("{end}")  # 从前端获取TODOList
    data_title = request.POST.get("title")
    user_token = request.POST.get("token")
    username = UserToken.objects.all().filter(user_token=user_token, is_alive=0)[0].username
    print(request.POST)
    template_manage_objs = models.TemplateForTODOmanage.objects.all().filter(sub_user=username).filter(name=data_title)
    if not template_manage_objs:
        # 如果没有这个，就创建一个
        pass
    print(template_manage_objs)
    template_manage_obj = template_manage_objs[0]
    models.ToDoListTemplate.objects.all().filter(sub_template=template_manage_obj).delete()
    print("data_get", data_get)
    for data_one_str in data_get.split("{end}"):
        if not data_one_str:
            continue
        text, _ = data_one_str.strip().split(", ")  # done就不要了
        models.ToDoListTemplate.objects.create(  # 创建新的ToDoList放到数据库中
            sub_template=template_manage_obj,
            sub_user=username,
            content=text,
        )
    return HttpResponse(json.dumps({"code": 20000, "data": "success"}))
