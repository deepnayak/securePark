# Generated by Django 3.1.7 on 2021-04-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_detectionvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectionvideo',
            name='name',
            field=models.CharField(default='default_name', max_length=100),
        ),
    ]
