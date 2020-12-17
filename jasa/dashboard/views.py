from django.shortcuts import render
from adminapp import models
from django.views.generic import TemplateView 
from django.http import HttpResponse
from django.db.models import Q

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

class SearchView(TemplateView):
    template_name = 'tampildashboard/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get('keyword')
        resulth = models.dataguru.objects.filter(
            Q(nama__contains=kw) |
            Q(gender__contains=kw)
            )
        print(resulth)
        context = {
            "resulth":resulth,
        }
        return context