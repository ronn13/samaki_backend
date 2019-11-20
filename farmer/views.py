from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .forms import *
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

import traceback
import logging

logging.basicConfig(filename='application.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logger = logging.getLogger()

def index(request):
    pickups = PickUp.objects.all()
    fields = PickUp._meta.get_fields()
    context = {
        'pickups': pickups,
        'fields': fields,
    }

    return render(request, 'dashboard.html', context)

@csrf_exempt
def pickup(request):
    farms = Farm.objects.all()
    if request.POST:
        form = PickUpForm(request.POST)
        try:
            if form.is_valid():
                form.save()
            else:
                logger.error(form.error)
        except:
            logger.error(traceback.format_exc())

        return redirect('index')
    else:
        form = PickUpForm()        
    
    context = {
        'form': form,
        'farms': farms,
    }

    return render(request, 'new_pickup.html', context)

def edit_pickup(request, pick_id=None):
    pickup_obj = get_object_or_404(PickUp, id=pick_id)

    form = PickUpForm(request.POST or None, instance = pickup_obj)

    if request.POST:
        if form.is_valid():
            pickup_obj = form.save(commit=False)
            pickup_obj.save()
            messages.success(request, "PickUp Updated")

            return redirect('index')
        else:
            context = {
                'form': form,
                'error': 'Record Not Updated Successfully. Please Try Again'
            }
            return render(request, 'edit_pickup.html', context)
    else:
        context = {
            'form': form,
        }

        return render(request, 'edit_pickup.html', context)

def farm(request, farm_id=None):
    pass

class PickupViewSet(viewsets.ModelViewSet):
    queryset = PickUp.objects.all()
    serializer_class = PickupSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

