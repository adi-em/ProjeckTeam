from django.shortcuts import render

# Create your views here.

def chome(request):
    return render(request, 'vcustomer/index.html')

def cdetail(request):
    return render(request, 'vcustomer/detail.html')