# Generated by Django 2.0.7 on 2018-08-15 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20180814_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='is_checked',
        ),
        migrations.RemoveField(
            model_name='shopproduct',
            name='pro_img',
        ),
        migrations.AlterField(
            model_name='address',
            name='address_area',
            field=models.TextField(blank=True, null=True, verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_contact',
            field=models.TextField(blank=True, null=True, verbose_name='联系人'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_detail',
            field=models.TextField(blank=True, null=True, verbose_name='详细住址'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_mail',
            field=models.TextField(blank=True, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_phone',
            field=models.TextField(blank=True, null=True, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='pro_count',
            field=models.IntegerField(verbose_name='商品数量'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='pro_price',
            field=models.IntegerField(verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='order',
            name='close_time',
            field=models.DateTimeField(verbose_name='交易关闭时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(verbose_name='订单创建时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_time',
            field=models.DateTimeField(verbose_name='付款结束时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_useRedPack',
            field=models.NullBooleanField(verbose_name='是否用了红包'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_comment',
            field=models.TextField(verbose_name='订单说明'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_num',
            field=models.TextField(verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_totalprice',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单总额'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.IntegerField(default=0, verbose_name='订单类型'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_time',
            field=models.DateTimeField(verbose_name='付款时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='已付金额'),
        ),
        migrations.AlterField(
            model_name='order',
            name='send_time',
            field=models.DateTimeField(verbose_name='发货时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_time',
            field=models.DateTimeField(verbose_name='订单更新时间'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_offer',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='订单优惠'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(verbose_name='商品数量'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='totalPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单项总额'),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='end_time',
            field=models.DateTimeField(verbose_name='截止时间'),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='group_code',
            field=models.TextField(verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='group_maxNum',
            field=models.IntegerField(default=10, verbose_name='团最大人数'),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='group_number',
            field=models.IntegerField(verbose_name='参团人数'),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='group_status',
            field=models.IntegerField(verbose_name='团的状态'),
        ),
        migrations.AlterField(
            model_name='productpicture',
            name='pictureType',
            field=models.IntegerField(default=0, verbose_name='图片类型'),
        ),
        migrations.AlterField(
            model_name='productpicture',
            name='url',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='type_level',
            field=models.IntegerField(default=0, verbose_name='商品类型层级'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='type_name',
            field=models.TextField(verbose_name='商品类型名称'),
        ),
        migrations.AlterField(
            model_name='redpack',
            name='is_used',
            field=models.BooleanField(verbose_name='是否被用了'),
        ),
        migrations.AlterField(
            model_name='redpack',
            name='red_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='红包数额'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_area',
            field=models.TextField(verbose_name='商店地区'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_man_avatar',
            field=models.TextField(blank=True, null=True, verbose_name='店长头像'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_man_name',
            field=models.TextField(blank=True, null=True, verbose_name='店长名称'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_man_phone',
            field=models.TextField(blank=True, null=True, verbose_name='店长电话'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_name',
            field=models.TextField(verbose_name='商店名称'),
        ),
        migrations.AlterField(
            model_name='shopbannar',
            name='bannar_url',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='商店海报'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='update_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='activityType',
            field=models.IntegerField(blank=True, null=True, verbose_name='活动类型'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='buyTimes',
            field=models.IntegerField(default=0, verbose_name='商品购买次数'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='活动商品说明'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='fullCount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='满减商品满价'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='fullMinus',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='满减商品减价'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='groupPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='拼团商品优惠价'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='limitCount',
            field=models.IntegerField(blank=True, null=True, verbose_name='限时商品总量'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='limitPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='限时商品优惠价'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='limitRemain',
            field=models.IntegerField(blank=True, null=True, verbose_name='限时商品剩余量'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='limitTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 15, 46, 55, 485585), verbose_name='限时商品截止时间'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='on_shelf',
            field=models.BooleanField(verbose_name='是否上架'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='pro_desc',
            field=models.TextField(blank=True, null=True, verbose_name='商品描述'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='pro_detail',
            field=models.TextField(blank=True, null=True, verbose_name='商品详情描述'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='pro_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='商品封面图'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='pro_name',
            field=models.TextField(verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='pro_norm',
            field=models.TextField(blank=True, null=True, verbose_name='商品规格'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='pro_origin_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='商品原价'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='pro_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='pro_producer',
            field=models.TextField(blank=True, null=True, verbose_name='商品产地'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='pro_remain',
            field=models.IntegerField(verbose_name='商品库存'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 15, 15, 46, 55, 478587), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.TextField(verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.TextField(verbose_name='用户名称'),
        ),
    ]