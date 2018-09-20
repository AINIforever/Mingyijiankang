# Generated by Django 2.0.7 on 2018-08-13 01:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20180813_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_redpack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.RedPack'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 13, 9, 52, 14, 852065)),
        ),
    ]
