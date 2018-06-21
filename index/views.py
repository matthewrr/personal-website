from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    context = {
        'abilities':Abilities.objects.all(),
        'education':Education.objects.all(),
        'experiences':Experience.objects.all(),
        'profile':Profile.objects.all()[0]
    }
    return render(request, 'index.html', context)