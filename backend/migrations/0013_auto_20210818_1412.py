# Generated by Django 3.1.7 on 2021-08-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20210818_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='buys',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='order_date',
            field=models.CharField(default='August 18, 202114:12:23', max_length=1000),
        ),
    ]
