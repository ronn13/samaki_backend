from django import forms
from django.contrib import admin
from .models import *

from easy_maps.widgets import AddressWithMapWidget

class FarmerAdmin(admin.ModelAdmin):
    pass

class FarmAdmin(admin.ModelAdmin):
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'farm_location': AddressWithMapWidget({'class': 'vCharField'})
            }

class PaymentsAdmin(admin.ModelAdmin):
    pass

class PickUpAdmin(admin.ModelAdmin):
    pass

admin.site.register(PickUp, PickUpAdmin)
admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(Payments, PaymentsAdmin)


