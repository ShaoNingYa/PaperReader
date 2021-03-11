# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class codeManage(models.Model):
    codeManageMainFlag = models.BooleanField()
    codeManageFirstNumber = models.CharField(max_length=20)
    codeManageSecondNumber = models.CharField(max_length=20)
    codeManageCodeName = models.CharField(max_length=30)
    codeManageCodeAuthor = models.CharField(max_length=20)
    codeManageIsShare = models.BooleanField()
    codeManageIsDelete = models.BooleanField()
    codeManageLanguage = models.CharField(max_length=20)
    codeManageSearchTimes = models.IntegerField()
    codeManageCheckTimes = models.IntegerField()
    codeManageDownloadTimes = models.IntegerField()
    codeManageCodeExplain = models.TextField()
    codeManageSavePosition = models.CharField(max_length=254)
    codeManageUploadTime = models.DateTimeField(auto_now=False,auto_now_add=True)
    def __unicode__(self):
        return self.codeManageCodeName

class codeLanguage(models.Model):
    codeLanguageType = models.CharField(max_length=20)
    codeLanguageTime = models.DateTimeField(auto_now_add=True)

class codeTag(models.Model):
    codeTagName = models.CharField(max_length=20)
    codeTagClickTimes = models.IntegerField()
    codeTagLastClick = models.DateTimeField(auto_now=True)

class codeTagRelation(models.Model):
    codeTagRelationiCodeID = models.CharField(max_length=20)
    codeTagRelationTagID = models.CharField(max_length=20)
    codeTagRelationTime = models.DateTimeField(auto_now_add=True)

class codeDiscuss(models.Model):
    codeDiscussSecondNumber = models.CharField(max_length=20)
    codeDiscussUserCreateID = models.CharField(max_length=20)
    codeDiscussUserReplyID = models.CharField(max_length=20)
    codeDiscussCreateDataTime = models.DateTimeField(auto_now_add=True)
    codeDiscussIsDelete = models.BooleanField()
    codeDiscussContent = models.TextField()
