# Generated by Django 4.0.3 on 2022-04-25 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petshop_app', '0003_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderplaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('dog', 'dog'), ('cat', 'cat')], max_length=100)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='petshop_app.customer')),
            ],
        ),
    ]
