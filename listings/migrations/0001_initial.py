# Generated by Django 4.2.4 on 2023-08-23 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('num_bedrooms', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('sqr_footage', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
