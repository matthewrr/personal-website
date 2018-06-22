from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    abilities = {
        'skills':Abilities.objects.filter(category='skills'),
        'tools':Abilities.objects.filter(category='tools'),
    }
    context = {
        'all_abilities':abilities,
        'education':Education.objects.order_by('start_date'),
        'experiences':Experience.objects.order_by('start_date'),
        'profile':Profile.objects.all()[0],
    }
    return render(request, 'index.html', context)