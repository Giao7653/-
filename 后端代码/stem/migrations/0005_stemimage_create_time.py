# Generated by Django 3.2.9 on 2022-09-10 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0004_stemimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='stemimage',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
    ]
