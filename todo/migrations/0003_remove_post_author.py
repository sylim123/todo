# Generated by Django 2.0.13 on 2019-05-15 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190514_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
