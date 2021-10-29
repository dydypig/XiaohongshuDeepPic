from django.contrib import admin
from .models import CloudPics,LocalPics, LocalPicsCache

# Register your models here.
admin.site.register(CloudPics)
admin.site.register(LocalPics)
admin.site.register(LocalPicsCache)
