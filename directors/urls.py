from django.urls import path
from . import views

urlpatterns  = [
    path('', views.index, name='index director'),
    path('create/', views.create, name='create director'),
    path('create/store/', views.store),
    path('edit/<int:id>', views.edit, name= 'edit director'),
    path('edit/update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('search/', views.search),
]