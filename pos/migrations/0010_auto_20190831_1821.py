# Generated by Django 2.2.4 on 2019-08-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0009_auto_20190831_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='resturant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='pos.Product'),
        ),
    ]
