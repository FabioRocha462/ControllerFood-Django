from django.urls import path
from . import views

urlpatterns  = [
    path('', views.index, name='index director'),
    path('create/', views.create, name='create director'),
    path('create/store', views.store),
]