# Generated by Django 2.1.2 on 2021-01-15 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_paper_view', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='papertranscodemanage',
            name='sub_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='paperreviewmanage',
            name='paper_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_paper_view.PaperBaseManage', verbose_name='所属论文'),
        ),
        migrations.AddField(
            model_name='paperreviewmanage',
            name='sub_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='paperreadmanage',
            name='paper_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_paper_view.PaperBaseManage', verbose_name='所属论文'),
        ),
        migrations.AddField(
            model_name='paperreadmanage',
            name='sub_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='paperkeywordconnect',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_paper_view.PaperKeyword', verbose_name='所属关键字'),
        ),
        migrations.AddField(
            model_name='paperkeywordconnect',
            name='paper_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_paper_view.PaperBaseManage', verbose_name='所属论文'),
        ),
        migrations.AddField(
            model_name='papercodemanage',
            name='paper_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_paper_view.PaperBaseManage', verbose_name='所属论文'),
        ),
        migrations.AddField(
            model_name='papercodemanage',
            name='sub_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='paperbasemanage',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_paper_view.PaperConference', verbose_name='所属会议'),
        ),
        migrations.AddField(
            model_name='paperbasemanage',
            name='sub_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
    ]
