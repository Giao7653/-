# Generated by Django 3.2.9 on 2022-11-26 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0021_delete_stemusercreate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stem',
            name='english',
        ),
    ]
