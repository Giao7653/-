# Generated by Django 3.2.9 on 2022-10-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0008_cloudplatform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcodesession',
            name='username',
            field=models.ImageField(default='', max_length=255, upload_to='static/avatar', verbose_name='账号'),
        ),
    ]
