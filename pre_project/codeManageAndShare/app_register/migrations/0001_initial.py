# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-26 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nomal_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomal_username', models.CharField(max_length=30)),
                ('nomal_usersex', models.CharField(max_length=5)),
                ('nomal_usergradeclass', models.CharField(max_length=100)),
                ('nomal_usernumber', models.CharField(max_length=20)),
                ('nomal_useremail', models.CharField(max_length=254)),
                ('nomal_useremailconfirm', models.CharField(max_length=10)),
                ('nomal_userconfirmid', models.CharField(max_length=10)),
                ('nomal_userImg', models.CharField(max_length=300)),
            ],
        ),
    ]
