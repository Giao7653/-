# Generated by Django 3.2.9 on 2022-10-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0015_stemsearchtimes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stemsearchtimes',
            name='stem_id',
        ),
        migrations.AddField(
            model_name='stemsearchtimes',
            name='search_content',
            field=models.CharField(default='', max_length=255, verbose_name='搜索内容'),
        ),
    ]
