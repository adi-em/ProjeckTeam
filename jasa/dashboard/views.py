from django.shortcuts import render
from adminapp import models

# Create your views here.

def home(request):
    dt = models.dataguru.objects.all()
    return render(request, 'tampildashboard/index.html',{ 
        'data' : dt,
    }) 

def profildashboard(request,id):
    task = models.dataguru.objects.filter(pk=id).first()
    return render(request, 'tampildashboard/profil.html',{ 
        'list' : task,
    })