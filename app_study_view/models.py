from django.db import models
from datetime import datetime
from app_user_manage.models import UserProfile


# Create your models here.


class ToDoList(models.Model):  # 待办事项
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)
    valid_time = models.DateField(auto_now=True, verbose_name="添加时间")
    content = models.CharField(max_length=200, verbose_name="待办内容")
    is_complete = models.IntegerField(choices=((0, "未完成"), (1, "已完成")), verbose_name="是否完成")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "待办事项"
        verbose_name_plural = verbose_name


class TemplateForTODOmanage(models.Model):  # 待办事项的模板
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="模板的名字")
    describe = models.CharField(max_length=200, verbose_name="模板的描述")
    is_shared = models.IntegerField(choices=((0, "不共享"), (1, "共享")), verbose_name="是否共享")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "模板管理"
        verbose_name_plural = verbose_name


class ToDoListTemplate(models.Model):  # 待办事项的模板
    sub_template = models.ForeignKey(TemplateForTODOmanage, verbose_name="所属模板类", on_delete=models.CASCADE)
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)
    content = models.CharField(max_length=200, verbose_name="待办内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "待办事项的模板"
        verbose_name_plural = verbose_name


class ToDoListLog(models.Model):  # 用来记录TODO的日志
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)
    content = models.CharField(max_length=16000, verbose_name="待办内容")  # max_length最大长度16383
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "待办事项的日志"
        verbose_name_plural = verbose_name
