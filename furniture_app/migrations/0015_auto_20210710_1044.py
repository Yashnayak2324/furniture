# Generated by Django 2.2 on 2021-07-10 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furniture_app', '0014_auto_20210708_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='Designerceiling_Image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Pvcdoor_Image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Pvcparition_Image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Tvcabinet_Image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Upvcwindow_Image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Wallpanelling_Image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Wardrobe_Image',
        ),
    ]
