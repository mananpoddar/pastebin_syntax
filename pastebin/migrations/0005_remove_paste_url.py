# Generated by Django 2.0 on 2018-08-19 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0004_auto_20180819_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paste',
            name='url',
        ),
    ]
