from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact = models.TextField()
    long = models.DecimalField(blank=True, null=True,  max_digits=8, decimal_places=3)
    lat = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=3)
    town = models.CharField(blank=True, null=True, max_length=100)
    city = models.CharField(blank=True , null=True,max_length=100)
    state = models.CharField(blank=True, null=True, max_length=100) 
    country = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.name
    
class DetectionVideo(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="default")
    path = models.CharField(max_length=1000, default=title)
    video = models.FileField(upload_to='')
     
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
         
    def __str__(self):
        return self.title


class CarProfile(models.Model):
    user = models.ForeignKey(User, default="", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    carno = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    carcolour = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class DetectionResult(models.Model):
    carno = models.CharField(max_length=150)
    user = models.ForeignKey(User, default="", on_delete=models.CASCADE, null=True, blank=True)