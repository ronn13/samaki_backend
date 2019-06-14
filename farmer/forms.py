from django.forms import ModelForm
from .models import *

class PickUpForm(ModelForm):
    class Meta:
        model = PickUp
        fields = '__all__'