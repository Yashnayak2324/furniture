# Generated by Django 2.2 on 2021-07-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture_app', '0013_auto_20210708_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='Designerceiling_Image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='images',
            name='Pvcdoor_Image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='images',
            name='Pvcparition_Image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='images',
            name='Tvcabinet_Image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='images',
            name='Upvcwindow_Image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='images',
            name='Wallpanelling_Image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='images',
            name='Wardrobe_Image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
    ]
