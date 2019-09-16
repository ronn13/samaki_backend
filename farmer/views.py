from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .forms import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt

import traceback

def index(request):
    pass

@csrf_exempt
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

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

