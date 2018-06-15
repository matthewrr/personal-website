from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    blank_stuff = []
    return render(request, 'index.html', {'blank_stuff': blank_stuff})