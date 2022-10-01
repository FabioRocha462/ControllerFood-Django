from django.urls import path
from . import views
urlpatterns  = [
    path('helloworld/',views.helloworld),
    path('hellofabio/',views.helloFabio),
    path('',views.viewAbout, name='about'),
]