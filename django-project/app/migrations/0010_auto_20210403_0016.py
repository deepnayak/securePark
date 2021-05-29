# Generated by Django 3.1.7 on 2021-04-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_detectionvideo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detectionvideo',
            options={'verbose_name': 'video', 'verbose_name_plural': 'videos'},
        ),
        migrations.RemoveField(
            model_name='detectionvideo',
            name='name',
        ),
        migrations.AddField(
            model_name='detectionvideo',
            name='title',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='detectionvideo',
            name='video',
            field=models.FileField(blank=True, upload_to='videos/'),
        ),
    ]