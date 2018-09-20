# Generated by Django 2.0.7 on 2018-08-14 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20180814_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopproduct',
            name='pro_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='图标'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='limitTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 14, 18, 1, 17, 954073)),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 14, 18, 1, 17, 949074)),
        ),
    ]