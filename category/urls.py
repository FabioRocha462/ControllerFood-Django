from django.urls import path
from . import views

urlpatterns  = [
    path('', views.index, name= "index category"),
    path('create/', views.create, name="create category"),
    path('create/store/', views.store),
    path('edit/<int:id>', views.edit, name='edit category'),
    path('edit/update/<int:id>', views.update),
    path('show/<int:id>', views.show, name='show category'),
    path('delete/<int:id>', views.delete),
]