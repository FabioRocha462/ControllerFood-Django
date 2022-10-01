from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("Hello World")

def helloFabio(request):
    return HttpResponse("Olá Fábio Rocha")

def viewAbout(request):
    return render(request, 'about/about.html')
