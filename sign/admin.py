from django.contrib import admin
from sign import models
# Register your models here.

# class EventAdmin(admin,ModelAdmin):



admin.site.register(models.Event)
admin.site.register(models.Guest)