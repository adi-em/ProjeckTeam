from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chome, name='chome'),
    path('profil/', views.profil, name='profilcustomer'),
    path('<id>/profilgr', views.profilgr, name='profil'),
    path('<no>/form', views.form),
    path('<no>/formklien', views.formklien),
]