# Generated by Django 3.2.9 on 2022-09-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0003_auto_20220921_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.TextField(default='', verbose_name='简介'),
        ),
    ]
