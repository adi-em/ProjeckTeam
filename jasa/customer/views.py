from django.shortcuts import render, redirect
from acounts.models import UserProfileInfo
from adminapp.models import dataguru, datamurid
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import imgform
# Create your views here.

def profil(request):
    usr  = UserProfileInfo.objects.filter(user=request.user.id).first()
    idx = usr.id
    profild = dataguru.objects.filter(no_id=idx).first()
    return render(request, 'vcustomer/profil2.html',{ 
        'profil' : profild,
    })

def profilmurid(request):
    usr  = UserProfileInfo.objects.filter(user=request.user.id).first()
    idx = usr.id
    profilm = datamurid.objects.filter(No_id=idx).first()
    return render(request, 'vcustomer/profilmurid.html',{ 
        'profil' : profilm,
    })

def chome(request):
    if request.user.is_authenticated:
        #x=UserProfileInfo.objects.aggregate(Max('nodata'))
        #y=x.objects.annotate(diff=F(x) + F(1))

        usr  = UserProfileInfo.objects.filter(user=request.user.id).first()
        dtgr = dataguru.objects.all()
        dtms = datamurid.objects.all()
        idx = usr.id
        foto = dataguru.objects.filter(no_id=idx).first()
        tmp = 0
        for p in dtgr:
            if p.no_id==idx:
                tmp += 1
        tmp2 = 0 
        for z in dtms:
            if z.No_id==idx:
                tmp2 += 1
        data = {
            'im' : foto,
            'usrx':usr,
            'data':dtgr,#data
            'temp':tmp,
            'temp2':tmp2,
            # 'cstm':priv,#custom
            # 'test': x
            # 'testy': y
        }
        return render(request, 'vcustomer/index.html',data)

def profilgr(request,id):
    task = dataguru.objects.filter(pk=id).first()
    return render(request, 'vcustomer/profil.html',{ 
        'list' : task,
    })

def form(request,no):
    x=no
    # if request.method == 'POST': 
    #     iform = imgform(data=request.POST)
    #     if iform.is_valid():
    #         # file is saved
    #         iform.save()
    if request.POST:
        dataguru.objects.create(
         nama=request.POST['nama'],
         alamat=request.POST['alamat'],
         biaya=request.POST['biaya'],
         no_id=x,
         nohp=request.POST['nohp'],
         usia=request.POST['usia'],
         link=request.POST['link'],
         foto=request.FILES['image'],
         portofolio=request.FILES['document']
         )
        
        return redirect('chome')
    uy = dataguru.objects.all()
    return render(request,'vcustomer/form.html',{ 
        'd' : uy,
        # 'iform':iform,
        })
def formklien(request,no):
    
    # if request.method == 'POST': 
    #     iform = imgform(data=request.POST)
    #     if iform.is_valid():
    #         # file is saved
    #         iform.save()
    if request.POST:
        datamurid.objects.create(
         nama=request.POST['nama'],
         alamat=request.POST['alamat'],
         No_id=no,
         nohp=request.POST['nohp'],

         )
        
        return redirect('chome')
    ey = dataguru.objects.all()
    return render(request,'vcustomer/formklien.html',{ 
        'e' : ey,
        # 'iform':iform,
        })