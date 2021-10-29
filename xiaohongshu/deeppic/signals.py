from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import LocalPics, LocalPicsCache
import os

@receiver(post_save, sender=User)
def create_user(sender,instance,created,**kwargs):
    if created:
        LocalPics.objects.create(user=instance)
    else:
        if hasattr(instance,'localpics'):
            instance.localpics.save()
        else:
            LocalPics.objects.create(user=instance)

@receiver(pre_delete,sender=LocalPics)
def delete_local_pic(sender,instance,**kwargs):
    if instance.imagelocal:
        os.remove(instance.imagelocal.path)
    if instance.imagedisplay:
        os.remove(instance.imagedisplay.path)

@receiver(post_save, sender=LocalPics)
def delete_local_pic_on_update(sender,instance,created,**kwargs):
    if created:
        if instance.imagelocal and instance.imagedisplay:
            LocalPicsCache.objects.create(localpics=instance, imagelocal=instance.imagelocal.file.name,imagedisplay=instance.imagedisplay.file.name)
        elif instance.imagelocal:
            LocalPicsCache.objects.create(localpics=instance, imagelocal=instance.imagelocal.file.name)
        elif instance.imagedisplay:
            LocalPicsCache.objects.create(localpics=instance, imagedisplay=instance.imagedisplay.file.name)
        else:
            LocalPicsCache.objects.create(localpics=instance)