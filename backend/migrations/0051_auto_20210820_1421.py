# Generated by Django 3.1.7 on 2021-08-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0050_auto_20210820_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='trend',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='order_date',
            field=models.CharField(default='August 20, 202114:21:04', max_length=1000),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='pay_date',
            field=models.CharField(default='August 20, 202114:21:04', max_length=1000),
        ),
        migrations.AlterField(
            model_name='sellhistory',
            name='date',
            field=models.CharField(default='August 20, 202114:21:04', max_length=1000),
        ),
    ]
