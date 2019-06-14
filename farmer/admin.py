from django.contrib import admin
from .models import *

class PickUpAdmin(admin.ModelAdmin):
    pass

admin.site.register(PickUp, PickUpAdmin)

