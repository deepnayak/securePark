# Generated by Django 3.1.7 on 2021-05-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_detectionresult_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectionvideo',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
