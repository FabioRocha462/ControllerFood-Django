import sched
from django.shortcuts import render, redirect

import directors

# Create your views here.

from .models import School
from directors.models import Director

def index(request):
    schools = School.objects.all().order_by('name')
    return render(request, 'schools/index.html', {'schools':schools})

def create(request):
    directors = Director.objects.all()
    return render(request, 'schools/create.html', {'directors':directors})

def store(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    nameDirector = request.POST['director']
    director = Director.objects.get(name = nameDirector)
    school = School(
        name = name,
        email = email,
        phone = phone,
        diretor = director
    )

    school.save()

    return redirect('/schools')

def edit(request, id):
    school = School.objects.get(id= id)
    directors = Director.objects.all()
    return render(request, 'schools/edit.html', {'school': school, 'directors':directors})

def update(request, id):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    nameDirector = request.POST['director']
    director = Director.objects.get(name= nameDirector)

    school = School.objects.get(id= id)
    school.name = name
    school.email = email
    school.phone = phone
    school.diretor = director

    school.save()

    return redirect('/schools')

def delete(request, id):
    school = School.objects.get(id= id)
    school.delete()
    return redirect('/schools')

