# Generated by Django 2.0.7 on 2018-08-15 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20180815_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='groupPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='拼团商品优惠价'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='limitPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='限时商品优惠价'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='limitTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 16, 12, 55, 904439), verbose_name='限时商品截止时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 15, 16, 12, 55, 901440), verbose_name='创建时间'),
        ),
    ]