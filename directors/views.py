from django.shortcuts import render, redirect

import directors
from .models import Director
# Create your views here.


def index(request):
    directors = Director.objects.all()
    return render(request,'director/index.html', {'directors':directors})

def create(request):
    return render(request, 'director/create.html')

def store(request):
    name, email, phone = request.POST['name'], request.POST['email'], request['phone']
    director = Director(
        name = name,
        email = email,
        phone = phone
    )
    director.save()
    return redirect('/director')