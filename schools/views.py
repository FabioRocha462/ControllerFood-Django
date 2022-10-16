import sched
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import directors

# Create your views here.

from .models import School
from directors.models import Director
from food.models import Food


def index(request):
    schools = School.objects.all().order_by('name')
    return render(request, 'schools/index.html', {'schools':schools})

def show(request, id):
    school = School.objects.get(id= id)
    foods = school.food_set.all()
    return render(request, 'schools/show.html', {'school':school, 'foods':foods})

def create(request):
    directors = Director.objects.all()
    return render(request, 'schools/create.html', {'directors':directors})

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
def delete(request, id):
    school = School.objects.get(id= id)
    school.delete()
    return redirect('/schools')

def search(request):
    name = request.GET['name']
    schoolName = School.objects.filter(name__contains = name)
    return render(request,'schools/index.html', {'schoolName':schoolName})

def foodSearch(request,id):
    school = School.objects.get(id= id)
    name = request.GET['name']
    foods = school.food_set.all()
    foodSearch = Food.objects.filter(name__contains = name)
    return render(request, 'schools/show.html', {'school':school, 'foodSearch':foodSearch, 'foods':foods})

def sendFood(request, idFood, idSchool):
    quantity = request.GET['quantity']
    food = Food.objects.get(id= idFood)
    schools = School.objects.get(id = idSchool)

    food.quantity = food.quantity - int(quantity)

    food.save()
    food.school.add(schools)

    return redirect('/schools')