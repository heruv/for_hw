from django.shortcuts import render
from django.http import HttpResponse # getting http response

# Create your views here.

def index(request):
    return HttpResponse("sucsesfully")