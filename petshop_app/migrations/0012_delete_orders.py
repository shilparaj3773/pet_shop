# Generated by Django 4.0.3 on 2022-04-27 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshop_app', '0011_orders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]