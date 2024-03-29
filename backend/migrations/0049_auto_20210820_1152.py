# Generated by Django 3.1.7 on 2021-08-20 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0048_auto_20210820_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='month',
            field=models.CharField(default='August', editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='invoice',
            name='month',
            field=models.CharField(default='August', editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='month',
            field=models.CharField(default='August', editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='month',
            field=models.CharField(default='August', editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='sellhistory',
            name='month',
            field=models.CharField(default='August', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='order_date',
            field=models.CharField(default='August 20, 202111:52:37', max_length=1000),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='pay_date',
            field=models.CharField(default='August 20, 202111:52:37', max_length=1000),
        ),
        migrations.AlterField(
            model_name='sellhistory',
            name='date',
            field=models.CharField(default='August 20, 202111:52:37', max_length=1000),
        ),
    ]
