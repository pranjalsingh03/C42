# Generated by Django 3.1.7 on 2021-08-18 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20210818_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.CharField(default='August 18, 2021', max_length=100),
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id2', models.CharField(default='#31BH20RA137T678', max_length=1000)),
                ('order_detail', models.TextField(default='', max_length=1000)),
                ('offer', models.CharField(default='', max_length=100)),
                ('pay_mode', models.CharField(default='Cash', max_length=100)),
                ('total_paid', models.CharField(default='', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.customer')),
            ],
        ),
    ]
