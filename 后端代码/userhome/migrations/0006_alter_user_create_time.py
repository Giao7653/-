# Generated by Django 3.2.9 on 2022-10-12 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0005_auto_20221009_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
