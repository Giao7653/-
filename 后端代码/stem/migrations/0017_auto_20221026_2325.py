# Generated by Django 3.2.9 on 2022-10-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0016_auto_20221022_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='stem',
            name='author',
            field=models.CharField(default='官方', max_length=255, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='stem',
            name='category',
            field=models.CharField(default='', max_length=255, verbose_name='类别'),
        ),
    ]
