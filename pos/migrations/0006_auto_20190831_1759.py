# Generated by Django 2.2.4 on 2019-08-31 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_auto_20190831_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='cat_name',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='product',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='sub_cat_name',
        ),
        migrations.AddField(
            model_name='category',
            name='resturant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.Restaurant'),
        ),
        migrations.AddField(
            model_name='product',
            name='resturant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.Restaurant'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='resturant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.Restaurant'),
        ),
    ]