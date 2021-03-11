from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    image = models.ImageField(upload_to="user/", max_length=200, verbose_name="头像", null=True, blank=True)
    nick_name = models.CharField(max_length=20, verbose_name="昵称", null=True, blank=True)
    birthday = models.DateTimeField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=(("girl", "女"), ("boy", "男")), max_length=10, verbose_name="性别")
    user_type = models.CharField(choices=(("teacher", "老师"), ("student", "学生"), ("other", "其他")), max_length=10,
                                 verbose_name="类别")
    address = models.CharField(max_length=200, verbose_name="家庭住址", null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name="手机", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20, verbose_name="邮箱验证码")
    email = models.EmailField(max_length=200, verbose_name="验证码邮箱")
    send_type = models.IntegerField(choices=((1, "register"), (2, "forget"), (3, "change")), verbose_name="验证码类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


class UserToken(models.Model):
    # TODO 先设定成这样吧，后面再改
    username = models.ForeignKey(UserProfile, verbose_name="所属用户", on_delete=models.CASCADE)
    user_token = models.CharField(max_length=200, verbose_name="用户令牌")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="生成时间")
    is_alive = models.IntegerField(choices=((0, "有效"), (1, "失效"), (2, "已注销")), default=0, verbose_name="令牌是否有效")
