from django.db import models
from datetime import datetime
from app_user_manage.models import UserProfile


# Create your models here.

class BadmintonOrder(models.Model):  # 羽毛球预定
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)
    name_of_order_person = models.CharField(max_length=200, verbose_name="预定人名字")
    number_of_venue = models.IntegerField(verbose_name="球场的号码")  # 1-12
    date_of_order = models.CharField(max_length=2000, verbose_name="预定时间")  # 指定的一天
    time_quantum = models.IntegerField(choices=((1, "早上"), (2, "中午"), (3, "晚上")), verbose_name="早中晚")
    time_of_order = models.IntegerField(verbose_name="时间段")  # 9-21
    pic_of_order = models.FileField(upload_to="static_files/badminton_order_pic_save", verbose_name="预定截图")
    remarks = models.CharField(max_length=2000, verbose_name="备注")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.date_of_order

    class Meta:
        verbose_name = "羽毛球场馆预定"
        verbose_name_plural = verbose_name
