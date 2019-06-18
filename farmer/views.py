from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .forms import *
from .serializers import *

import traceback

def pickup(request):
    if request.POST:
        form = PickUpForm(request.POST)
        print(request.POST)
        try:
            if form.is_valid():
                form.save()
        except:
            print(traceback.format_exc())

        return HttpResponse("True")

class PickupViewSet(viewsets.ModelViewSet):
    queryset = PickUp.objects.all()
    serializer_class = PickupSerializer