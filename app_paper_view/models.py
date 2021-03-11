from django.db import models
from datetime import datetime
from app_user_manage.models import UserProfile


# Create your models here.
class PaperConference(models.Model):  # 存储会议
    name = models.CharField(max_length=200, verbose_name="会议名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "会议、期刊"
        verbose_name_plural = verbose_name


class PaperBaseManage(models.Model):
    name = models.CharField(max_length=200, verbose_name="论文名称")
    author = models.CharField(max_length=200, verbose_name="论文作者")
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)  # 哪个用户添加的此篇论文
    conference = models.ForeignKey(PaperConference, verbose_name="所属会议", on_delete=models.CASCADE)
    conference_year = models.IntegerField(verbose_name="论文年份")
    paper_file = models.FileField(upload_to="static_files/paper_file_save", verbose_name="论文存储")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "论文基础管理数据库"
        verbose_name_plural = verbose_name


class PaperKeyword(models.Model):  # 存储论文关键字
    keyword = models.CharField(max_length=20, verbose_name="关键字")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = "关键字"
        verbose_name_plural = verbose_name


class PaperKeywordConnect(models.Model):  # 存储论文关键字中的联系
    paper_name = models.ForeignKey(PaperBaseManage, verbose_name="所属论文", on_delete=models.CASCADE)
    keyword = models.ForeignKey(PaperKeyword, verbose_name="所属关键字", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.paper_name.name

    class Meta:
        verbose_name = "关键字连接"
        verbose_name_plural = verbose_name


class PaperReviewManage(models.Model):  # 评论
    paper_name = models.ForeignKey(PaperBaseManage, verbose_name="所属论文", on_delete=models.CASCADE)
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)  # 哪个用户添加的此篇论文
    starts = models.IntegerField(choices=((1, "*"), (2, "**"), (3, "***")), verbose_name="评价")
    review_text = models.CharField(max_length=200, verbose_name="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.review_text

    class Meta:
        verbose_name = "论文用户评论"
        verbose_name_plural = verbose_name


class PaperTransCodeManage(models.Model):  # 翻译和代码(原论文的代码)
    paper_name = models.ForeignKey(PaperBaseManage, verbose_name="所属论文", on_delete=models.CASCADE)
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)  # 哪个用户添加的此篇论文
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    trans_file = models.FileField(upload_to="app_paper_view", verbose_name="论文翻译存储（markdown格式）")

    def __str__(self):
        return self.paper_name.name

    class Meta:
        verbose_name = "论文翻译"
        verbose_name_plural = verbose_name


class PaperReadManage(models.Model):  # 论文的浏览
    paper_name = models.ForeignKey(PaperBaseManage, verbose_name="所属论文", on_delete=models.CASCADE)
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)  # 哪个用户添加的此篇论文
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    add_type = models.IntegerField(choices=((1, "时间自动保存"), (2, "点击自动保存")), verbose_name="操作类型")
    read_process = models.IntegerField(default=1, verbose_name="浏览进度（记录页数）")
    read_zoom = models.IntegerField(default=100, verbose_name="缩放大小")

    def __str__(self):
        # 不能用外键作为表名
        return self.paper_name.name

    class Meta:
        verbose_name = "论文浏览进度"
        verbose_name_plural = verbose_name


class PaperCodeManage(models.Model):  # 根据论文，用户自己编写的代码
    paper_name = models.ForeignKey(PaperBaseManage, verbose_name="所属论文", on_delete=models.CASCADE)
    sub_user = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)  # 哪个用户添加的此篇论文
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    add_version = models.CharField(max_length=10, verbose_name="代码版本")

    def __str__(self):
        return self.paper_name.name

    class Meta:
        verbose_name = "论文用户自定义代码"
        verbose_name_plural = verbose_name
