# Generated by Django 3.2.9 on 2022-10-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0017_auto_20221026_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStemSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=255, verbose_name='用户名')),
                ('stem', models.CharField(default='', max_length=255, verbose_name='用户发布梗')),
                ('is_agree', models.BooleanField(default=0, verbose_name='是否同意')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户待发布梗管理',
                'verbose_name_plural': '用户待发布梗管理',
            },
        ),
    ]
