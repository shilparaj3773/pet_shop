# Generated by Django 4.0.3 on 2022-04-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop_app', '0004_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='city',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='state',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='order_status',
            field=models.IntegerField(default=False),
        ),
    ]
