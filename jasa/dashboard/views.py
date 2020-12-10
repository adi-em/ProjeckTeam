from django.shortcuts import render
from adminapp import models

# Create your views here.

def home(request):
    dt = models.dataguru.objects.all()
    return render(request, 'tampildashboard/index.html',{ 
        'data' : dt,
    }) 

def detail(request):
    return render(request, 'tampildashboard/detail.html')