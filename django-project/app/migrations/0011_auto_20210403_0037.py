# Generated by Django 3.1.7 on 2021-04-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210403_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectionvideo',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
