# Generated by Django 2.2.4 on 2019-08-31 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0008_auto_20190831_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='resturant',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='resturant',
        ),
    ]
