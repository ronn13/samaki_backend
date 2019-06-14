from django.shortcuts import render, HttpResponse
from .forms import *

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
