# Generated by Django 3.2.9 on 2022-09-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.CharField(default='', max_length=255, verbose_name='用户头像'),
        ),
    ]
