from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('', views.chome, name='chome'),
    path('detail/', views.cdetail, name='cdetail'),
]