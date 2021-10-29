from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class CloudPics(models.Model):
    image = models.ImageField(upload_to='cloud_pics',null=True, blank=True)

    def __str__(self):
        return str(self.pk) + '-' + self.image.name

    def get_absolute_url(self):
        return reverse('home')

class LocalPics(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    imagelocal = models.ImageField(default =None,upload_to='local_pics',null=True, blank=True)
    imagecloud = models.ImageField(default =None,upload_to='local_pics',null=True, blank=True)
    imagedisplay = models.ImageField(default =None,upload_to='local_pics',null=True, blank=True)

    def __str__(self):
        return self.user.username + '-' + 'Pictures'
    
    def get_absolute_url(self):
        return reverse('home')

class LocalPicsCache(models.Model):
    localpics = models.OneToOneField(LocalPics,on_delete=models.CASCADE)
    imagelocal = models.TextField(default=None,null=True, blank=True)
    imagedisplay = models.TextField(default=None,null=True, blank=True)

    def __str__(self):
        return self.localpics.user.username + '-' + 'Pictures Caches'

