# Generated by Django 3.1.7 on 2021-08-19 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0028_auto_20210819_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='order_date',
            field=models.CharField(default='August 19, 202107:47:51', max_length=1000),
        ),
    ]
