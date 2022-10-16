from django.shortcuts import render, redirect

import directors
from .models import Director
# Create your views here.
from django.views.decorators.csrf
import requires_csrf_token

def index(request):
    directors = Director.objects.all().order_by('name')
    return render(request,'director/index.html', {'directors':directors})

def create(request):
    return render(request, 'director/create.html')

@requires_csrf_token
def store(request):
    
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    director = Director(
        name = name,
        email = email,
        phone = phone
    )
    director.save()
    return redirect('/director')

def edit(request, id):
    director = Director.objects.get(id= id)
    return render(request, 'director/edit.html', {'director': director})

@requires_csrf_token
def update(request, id):
    director = Director.objects.get(id= id)
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']

    director.name = name
    director.email = email
    director.phone = phone

    director.save()

    return redirect('/director')

def delete(request, id):
    director = Director.objects.get(id= id)
    director.delete()
    return redirect('/director')

def search(request):
    name = request.GET['name']
    directorName = Director.objects.filter(name__contains = name)
    return render(request, 'director/index.html', {'directorName':directorName})
