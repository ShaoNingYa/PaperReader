# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class nomal_user(models.Model):
    #nomal_userid = models.AutoField()
    nomal_username = models.CharField(max_length=30)
    nomal_usersex = models.CharField(max_length=5)
    nomal_usergradeclass = models.CharField(max_length=100)
    nomal_usernumber = models.CharField(max_length=20)
    #nomal_usercreatedate = models.DateTimeField(auto_now=False,auto_now_add=True)
    #nomal_userpassword = models.CharField(max_length=30)
    #nomal_userdownload = models.CharField(max_length=100)
    #nomal_userfocususer = models.CharField(max_length=100)
    nomal_useremail = models.CharField(max_length=254)
    nomal_useremailconfirm = models.CharField(max_length=10)
    nomal_userconfirmid = models.CharField(max_length=10)
    nomal_userImg = models.CharField(max_length=300)
