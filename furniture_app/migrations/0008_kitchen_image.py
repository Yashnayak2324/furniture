# Generated by Django 2.2 on 2021-07-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture_app', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(default='', upload_to='images/')),
            ],
        ),
    ]
