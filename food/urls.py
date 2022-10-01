from django.urls import path
from . import views

urlpatterns  = [
    path('',views.index, name='index food'),
    path('create/',views.create, name='create food'),
    path('create/store/', views.store),
    path('show/<int:id>', views.show, name='show food'),
    path('edit/<int:id>', views.edit, name='edit food'),
    path('edit/update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('search/', views.search),
]