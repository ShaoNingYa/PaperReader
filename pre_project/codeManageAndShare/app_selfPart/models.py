# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class selfPartMessage(models.Model):
    #selfPartMessageID = models.AutoField()
    selfPartMessageCreateTime = models.DateTimeField(auto_now=False, auto_now_add=True)
    selfPartMessageSendUserID = models.CharField(max_length=20)
    selfPartMessageReceUserID = models.CharField(max_length=20)
    selfPartMessageIsNew = models.BooleanField()
    selfPartMessageIsDeleteByRece = models.BooleanField()
    selfPartMessageIsDeleteBySend = models.BooleanField()
    selfPartMessageContent = models.TextField()

class selfPartMyFriends(models.Model):
    selfPartFriendDoneTime = models.DateTimeField(auto_now=False,auto_now_add=True)
    selfPartOwnID = models.CharField(max_length=20)
    selfPartFriendID = models.CharField(max_length=20)

class selfPartFocusRelation(models.Model):
    selfPartFocusRelationOwnID = models.CharField(max_length=20)
    selfPartFocusRelationUserID = models.CharField(max_length=20)
    selfPartFocusRelationCodeID = models.CharField(max_length=20)
    selfPartFocusRelationTime = models.DateTimeField(auto_now_add=True)

class selfPartUserDynamic(models.Model):
    selfPartUserDynamicUserID = models.CharField(max_length=10)
    selfPartUserDynamicType = models.CharField(max_length=30)
    selfPartUserDynamicPic = models.CharField(max_length=20)
    selfPartUserDynamicExplain = models.TextField()
    selfPartUserDynamicCodeID = models.CharField(max_length=10)
    selfPartUserDynamicTime = models.DateTimeField(auto_now_add=True)
