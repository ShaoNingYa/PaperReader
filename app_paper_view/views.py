# coding: utf-8

import json
import time
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app_paper_view import models
from app_user_manage.models import UserToken
from app_user_manage.models import UserProfile


# Create your views here.


def index(request):
    return HttpResponse("论文阅读的主页，用于管理所有的论文")


@csrf_exempt
def history(request):
    # print(request.POST)
    history_return = []
    data_get = models.PaperReadManage.objects.all().filter(
        sub_user=UserToken.objects.all().filter(user_token=request.POST.get("token"), is_alive=0)[0].username)
    for data_one in data_get:
        his_one = {
            "paper_id": str(data_one.paper_name.id),
            "paper_title": str(data_one.paper_name.name),
            "paper_path": str(data_one.paper_name.paper_file).split("static_files/paper_file_save/")[-1],
            # .replace("static_files/paper_file_save/", ""),
            "paper_user": str(data_one.sub_user.username),
            "paper_data": str(data_one.add_time.strftime("%Y-%m-%d %H:%M:%S")),
            "paper_info": str(data_one.get_add_type_display()),
            "paper_page": str(data_one.read_process),
            "paper_zoom": str(data_one.read_zoom)
        }
        history_return.append(his_one.copy())
    history_return_temp = history_return[::-1].copy()
    # 每篇论文只取出最新的一条浏览记录
    list_temp = []
    history_return = []
    for his_one in history_return_temp:
        if his_one.get("paper_id") not in list_temp:
            history_return.append(his_one)
            list_temp.append(his_one.get("paper_id"))
    return HttpResponse(json.dumps({"code": 20000, "data": history_return}))


@csrf_exempt
def history_one_paper(request):
    # print(request.POST)
    history_return = []
    data_get = models.PaperReadManage.objects.all() \
        .filter(sub_user=UserToken.objects.all().filter(user_token=request.POST.get("token"), is_alive=0)[0].username) \
        .filter(paper_name=request.POST.get("paper_id"))
    paper_name = "历史浏览记录："
    for data_one in data_get:
        paper_name = str(data_one.paper_name.name)
        history_return.append(str(data_one.read_process))
        # his_one = {
        #     "paper_id": str(data_one.paper_name.id),
        #     "paper_title": str(data_one.paper_name.name),
        #     "paper_path": str(data_one.paper_name.paper_file).replace("static_files/paper_file_save/", ""),
        #     "paper_user": str(data_one.sub_user.username),
        #     "paper_data": str(data_one.add_time.strftime("%Y-%m-%d %H:%M:%S")),
        #     "paper_info": str(data_one.get_add_type_display()),
        #     "paper_page": str(data_one.read_process),
        #     "paper_zoom": str(data_one.read_zoom)
        # }
    print(history_return)
    return HttpResponse(json.dumps({"code": 20000, "data": history_return, "paper_name": paper_name}))


# dddd = { "code": 20000, "data": { "total": 100, "items": [ { "paper_id": 1, "timestamp": 621870193097,
# "author": "Timothy", "reviewer": "Cynthia", "title": "Gzei Dzvufntea Fwexloovs Fadmebwya Ldhirhro Vehxahflt
# Pnbjilbgkc Dwv", "content_short": "mock data", "content": "<p>I am testing data, I am testing data.</p><p><img
# src=\"https://wpimg.wallstcn.com/4c69009c-0fd4-4153-b112-6cb53d1cf943\"></p>", "forecast": 62.82, "importance": 3,
# "type": "JP", "status": "draft", "display_time": "2006-12-15 19:47:39", "comment_disabled": True, "pageviews":
# 2186, "image_uri": "https://wpimg.wallstcn.com/e4558086-631c-425c-9430-56ffb46e70b3", "platforms": [ "a-platform" ]
# }] } }


def getHistoryPageByPaper(paper_obj):
    obj_get = models.PaperReadManage.objects.filter(paper_name=paper_obj).order_by('add_time')
    if obj_get:
        return {
            "page": obj_get.last().read_process,
            "zoom": obj_get.last().read_zoom
        }
    return {
        "page": 0,
        "zoom": 100
    }


def getAllConferenceName() -> list:
    allName = list(set([con_one.name for con_one in models.PaperConference.objects.all()]))
    return allName


def getAllPaperLabelName() -> list:
    allName = list(set([label_one.label_text for label_one in models.PaperLabel.objects.all()]))
    return allName


@csrf_exempt
def paper_mine(request):
    if request.method == 'GET':
        # print(request.GET)  # {'page': ['1'], 'limit': ['10'], 'sort': ['+id']}
        history_return = []
        print()
        username = UserToken.objects.all().filter(user_token=request.GET.get("token"), is_alive=0)[0].username
        data_get = models.PaperBaseManage.objects.all().filter(sub_user=username)
        paper_label_obj = models.PaperLabelConnect.objects.all().filter(sub_user=username)
        for data_one in data_get:
            paper_label = [_l.sub_label.label_text for _l in paper_label_obj.filter(sub_paper=data_one)][-1:]
            his_one = {
                "paper_id": str(data_one.id),
                "paper_title": str(data_one.name),
                "paper_data": str(data_one.conference_year),
                "paper_author": str(data_one.author),
                "paper_sub_user": str(data_one.sub_user),
                "paper_conference": str(data_one.conference),
                "paper_label": "".join(paper_label),
                "paper_history": getHistoryPageByPaper(data_one),
                "paper_path": str(data_one.paper_file).split("static_files/paper_file_save/")[-1],
                # .replace("static_files/paper_file_save/", ""),
                "paper_data_upload": int(data_one.add_time.timestamp()),
            }

            history_return.append(his_one.copy())
        history_return = history_return
        data = {
            "total": len(history_return),
            "items": history_return,
            "all_conference": [{"text": con_one, "value": con_one} for con_one in getAllConferenceName()],
            "all_label": [{"text": con_one, "value": con_one} for con_one in getAllPaperLabelName()]
        }
        return HttpResponse(json.dumps({"code": 20000, "data": data}))
        # return HttpResponse(json.dumps(dddd))


def paper_conference(request):
    from app_paper_view.static_for_conference.process import get_data
    data = get_data(
        pre_path="/home/ubuntu/my_pro/PaperReader/app_paper_view/static_for_conference/")  # 在部署到apache服务器上后修改成完整路径
    sub_label = list(set([data_one['sub'] for data_one in data]))
    sub_label = [{"text": sub_one, "value": sub_one} for sub_one in sub_label]
    return HttpResponse(json.dumps({"code": 20000, "data": data, "sub_label": sub_label}))


@csrf_exempt
def paper_upload_file(request):
    print("先上传文件")
    user_token = request.POST.get('token')
    pdf_file = request.FILES.get('file')
    file_type = pdf_file.name.split('.')[-1]
    if not file_type == "pdf":  # 上传文件如果不是PDF格式，直接返回
        return HttpResponse(json.dumps("fail"))
    pdf_file.name = time.strftime("%Y-%m-%d-%H-%M-%S.") + file_type
    token_obj = UserToken.objects.all().filter(user_token=user_token, is_alive=0)
    if token_obj:
        if pdf_file:
            obj_create = models.PaperBaseManage.objects.create(
                name="temp_name",
                author="temp_author",
                sub_user=token_obj[0].username,
                conference=models.PaperConference.objects.all().filter(id=3)[0],
                conference_year=2000,
                paper_file=pdf_file
            )
            return HttpResponse(json.dumps({"code": 20000, "id": obj_create.id}))
    return HttpResponse(json.dumps("fail"))


def get_all_conference(request):
    all_con_obj = models.PaperConference.objects.all()
    return_result = []
    for con_one in all_con_obj:
        return_result.append({
            "conference_name": con_one.name,
            "conference_id": con_one.id,
        })
    return HttpResponse(json.dumps({"code": 20000, "data": return_result}))


def get_all_label(request):
    all_con_obj = models.PaperLabel.objects.all()
    return_result = []
    for con_one in all_con_obj:
        return_result.append({
            "label_text": con_one.label_text,
            "label_id": con_one.id,
        })
    return HttpResponse(json.dumps({"code": 20000, "data": return_result}))


def get_all_paper_label(request):
    all_label_obj = models.PaperLabel.objects.all()
    return_result = []
    for one_label in all_label_obj:
        return_result.append({
            "label_text": one_label.label_text,
            "label_id": one_label.id,
        })
    return HttpResponse(json.dumps({"code": 20000, "data": return_result}))


def get_conference_id_by_name(request):
    all_con_obj = models.PaperConference.objects.all().filter(name=request.GET.get("conference_name"))
    if all_con_obj:
        return HttpResponse(json.dumps({"code": 20000, "id": all_con_obj[0].id}))
    return HttpResponse(
        json.dumps({"code": 20000, "id": models.PaperConference.objects.all().filter(name="other")[0].id}))


def get_label_id_by_name(request):
    label_text = request.GET.get("label_text")
    print("label_text", label_text)
    if label_text.strip() != "":
        all_con_obj = models.PaperLabel.objects.all().filter(label_text=label_text)
        print("all_con_obj", all_con_obj)
        if all_con_obj:
            return HttpResponse(json.dumps({"code": 20000, "id": all_con_obj[0].id}))
    return HttpResponse(
        json.dumps({"code": 20000, "id": models.PaperLabel.objects.all().filter(label_text="None")[0].id}))


@csrf_exempt
def paper_update(request):
    models.PaperBaseManage.objects.all().filter(id=request.POST.get('id')).update(
        name=request.POST.get('name'),
        author=request.POST.get('author'),
        conference=models.PaperConference.objects.all().filter(id=request.POST.get('conference'))[0],
        conference_year=request.POST.get('conference_year')
    )
    return HttpResponse(json.dumps({"code": 20000, "data": "success"}))


def paper_read_update(request):
    """
    :param request: 1.user_Token, 2.paper_ID, 3.read_process, 4.read_zoom, 5.add_type
    :return:
    """
    # print(request.GET.get("paper_ID"))
    # print(request.GET.get("user_ID"))
    # print(request.GET.get("read_process"))
    # print(request.GET.get("read_zoom"))
    # print(request.GET.get("add_type"))
    print(request.GET.get("user_Token"))
    print(UserToken.objects.all().filter(user_token=request.GET.get("user_Token"), is_alive=0))
    print(UserToken.objects.all())
    models.PaperReadManage.objects.create(
        paper_name=models.PaperBaseManage.objects.all().filter(id=request.GET.get("paper_ID"))[0],
        # sub_user=UserProfile.objects.all().filter(id=request.GET.get("user_ID"))[0],
        sub_user=UserToken.objects.all().filter(user_token=request.GET.get("user_Token"), is_alive=0)[0].username,
        add_type=request.GET.get("add_type"),
        read_process=request.GET.get("read_process"),
        read_zoom=request.GET.get("read_zoom")
    )
    return HttpResponse(json.dumps({"code": 20000, "data": "success"}))
