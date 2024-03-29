# Generated by Django 4.0.3 on 2022-04-22 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop_app', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('dog', 'dog'), ('cat', 'cat')], max_length=100)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
