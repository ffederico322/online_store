from django.contrib import admin
from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about')
]

