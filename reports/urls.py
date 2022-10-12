from django.urls import path
from . import views

urlpatterns  = [
    path('', views.allfood, name='index report'),
    path('forcategory/', views.forcategory),
    path('fordate/', views.fordate),
]