# Generated by Django 3.1.7 on 2021-05-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_detectionvideo_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectionvideo',
            name='video',
            field=models.FileField(upload_to=''),
        ),
    ]
