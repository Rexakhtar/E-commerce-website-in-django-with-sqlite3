# Generated by Django 2.1.5 on 2019-09-08 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190907_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='photo_slider',
        ),
    ]
