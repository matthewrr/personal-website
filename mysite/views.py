from django.shortcuts import render
from django.http import HttpResponseRedirect

def redirect_root(request):
    return HttpResponseRedirect('/index/')