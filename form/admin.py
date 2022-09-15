from django.contrib import admin

from form.models import data

class dataAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(data,dataAdmin)
