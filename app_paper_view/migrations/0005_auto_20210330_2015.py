# Generated by Django 2.2 on 2021-03-30 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_paper_view', '0004_paperbasemanage_conference_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperbasemanage',
            name='conference_year',
            field=models.IntegerField(verbose_name='论文年份'),
        ),
    ]
