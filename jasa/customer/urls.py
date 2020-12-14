from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chome, name='chome'),
    path('detail/', views.cdetail, name='cdetail'),
    path('<id>/profilgr', views.profilgr),
    path('<no>/form', views.form),
    path('<no>/formklien', views.formklien),
]