# Generated by Django 3.2.9 on 2022-10-12 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0012_auto_20221012_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stemrecommend',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
