from django.contrib import admin
from .models import Watch, Accessory, Service

# Register your models here.
admin.site.register(Watch)
admin.site.register(Accessory)
admin.site.register(Service)