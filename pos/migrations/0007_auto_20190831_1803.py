# Generated by Django 2.2.4 on 2019-08-31 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_auto_20190831_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='orderitem',
            new_name='order',
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='resturant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.Restaurant'),
        ),
    ]
