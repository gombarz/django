from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('elso/', views.elso, name='elso'),
    path('masodik/', views.masodik, name='masodik'),
    path('harmadik/', views.harmadik, name='harmadik'),
]
