from django.urls import path
from . import views

urlpatterns  = [
    path('', views.index, name='index schools'),
    path('create/', views.create, name='create schools'),
    path('create/store/', views.store),
    path('edit/<int:id>', views.edit, name='edit school'),
    path('edit/update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]