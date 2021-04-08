# coding: utf-8
import time
import json
import logging
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date, timedelta
from app_activities_view import models
from app_user_manage.models import UserToken
from app_user_manage.models import UserProfile

logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


# Create your views here.


def index(request):
    return HttpResponse("活动管理的主页")


@csrf_exempt
def order_get_all(request):
    """获取某一天所有的羽毛球预定数据
    :param request:
    :return:
    """
    str_of_day = [(date.today() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(3)]  # 今天、明天、后天的字符串数组
    i_d = int(request.POST.get('one_day'))
    str_of_one_day = str_of_day[i_d - 1]
    number_of_gym = 12
    order_today = {  # 1-1-1-1: 第几天-早中晚-场馆-时间段   [1-3]-[1-3]-[1-12]-[9-21]
        'data_morning': [{'id': i_t,
                          'data_detail': [{'order_id': '{}-1-{}-{}'.format(i_d, i_t, i_g), 'is_order': 'None'} for i_g
                                          in range(*[9, 12])]} for i_t in range(*[1, number_of_gym + 1])],
        'data_afternoon': [{'id': i_t,
                            'data_detail': [{'order_id': '{}-2-{}-{}'.format(i_d, i_t, i_g), 'is_order': 'None'} for i_g
                                            in range(*[12, 17])]} for i_t in range(*[1, number_of_gym + 1])],
        'data_night': [{'id': i_t,
                        'data_detail': [{'order_id': '{}-3-{}-{}'.format(i_d, i_t, i_g), 'is_order': 'None'} for i_g in
                                        range(*[17, 22])]} for i_t in range(*[1, number_of_gym + 1])]
    }
    data_get = models.BadmintonOrder.objects.all().filter(date_of_order=str_of_one_day)
    for data_one in data_get:
        # item_one = {
        #     "name_of_order_person": str(data_one.name_of_order_person),
        #     "number_of_venue": data_one.number_of_venue,
        #     "time_quantum": data_one.time_quantum,  # 早中晚 1-3
        #     "time_of_order": data_one.time_of_order,  # 几点
        #     "pic_of_order": str(data_one.pic_of_order),
        #     "remarks": str(data_one.remarks),
        # }
        # order_data_all.append(item_one.copy())
        time_quantum = ['data_morning', 'data_afternoon', 'data_night'][data_one.time_quantum - 1]
        time_start = data_one.time_of_order - [9, 12, 17][data_one.time_quantum - 1]  # 计算这个时刻是[早上]的第几个（9点是早上的第一个）
        # print(data_one.time_of_order, data_one.time_quantum, time_start)
        name_order_person = str(data_one.name_of_order_person)
        pic_url = str(data_one.pic_of_order).split("static_files/")[-1]
        order_today[time_quantum][data_one.number_of_venue - 1]['data_detail'][time_start][
            'is_order'] = name_order_person
        order_today[time_quantum][data_one.number_of_venue - 1]['data_detail'][time_start]['pic_url'] = pic_url
        order_today[time_quantum][data_one.number_of_venue - 1]['data_detail'][time_start]['remarks'] = str(data_one.remarks)
    return HttpResponse(json.dumps({"code": 20000, "date": time.strftime("%Y-%m-%d"), "data": order_today}))


@csrf_exempt
def order_pic_upload(request):
    user_token = request.POST.get('token')
    pic_file = request.FILES.get('file')
    order_name = request.POST.get('order_name')
    order_remarks = request.POST.get('order_remarks')
    order_id = request.POST.get('id_one_part')
    # print(user_token, pic_file, order_id, order_name, order_remarks)
    token_obj = UserToken.objects.all().filter(user_token=user_token, is_alive=0)
    str_of_day = [(date.today() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(3)]
    pic_file.name = time.strftime("%Y-%m-%d_") + order_id + pic_file.name.split('.')[-1]
    if token_obj and pic_file and order_name and order_id:
        # 先解析order_id
        date_of_order, time_quantum, number_of_venue, time_of_order = order_id.split("-")
        # print(number_of_venue, date_of_order, time_quantum, time_of_order)
        obj_create = models.BadmintonOrder.objects.create(
            sub_user=token_obj[0].username,
            name_of_order_person=order_name,
            number_of_venue=number_of_venue,
            date_of_order=str_of_day[int(date_of_order) - 1],  # 指定的一天
            time_quantum=time_quantum,
            time_of_order=time_of_order,  # 9-21
            pic_of_order=pic_file,
            remarks=order_remarks
        )
    return HttpResponse(json.dumps({"code": 20000, "id": "obj_create.id"}))


@csrf_exempt
def order_one_del(request):
    user_token = request.POST.get('token')
    order_id = request.POST.get('id_one_part')
    token_obj = UserToken.objects.all().filter(user_token=user_token, is_alive=0)
    date_of_order, time_quantum, number_of_venue, time_of_order = order_id.split("-")
    str_of_day = [(date.today() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(3)][int(date_of_order) - 1]

    data_get_from_db = models.BadmintonOrder.objects.all().filter(date_of_order=str_of_day)  # 获取数据库中这一天的数据
    obj = data_get_from_db.filter(time_quantum=time_quantum)  # 找到
    obj = obj.filter(number_of_venue=number_of_venue)  # 找到
    obj = obj.filter(time_of_order=time_of_order)  # 找到
    obj.delete()  # 将匹配到的删掉
    # print("删除", str_of_day, number_of_venue, time_quantum, time_of_order)
    return HttpResponse(json.dumps({"code": 20000, "res": "success"}))
