from django.shortcuts import render,redirect, get_object_or_404
import json
import category
from .models import Food
from category.models import Category
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    food = Food.objects.all().order_by('name')
    return render(request, 'food/index.html', {'food': food})

def create(request):
    categorys = Category.objects.all()
    return render( request, 'food/create.html', {'categorys':categorys})

@csrf_exempt
def store(request):
    name = request.POST['name']
    validity = request.POST['validity']
    quantity = request.POST['quantity']
    weight = request.POST['weight']
    
    name_category = request.POST['category']
    category = Category.objects.get(name= name_category)
    food = Food(
        name= name,
        validity = validity,
        quantity = quantity,
        weight = weight,
        category = category
    )

    food.save()
    return redirect('/')

def show(request, id):
    food = Food.objects.get(id= id)
    return render( request, 'food/show.html', {'food': food})

def edit(request, id):
    food = Food.objects.get(id=id)
    categorys = Category.objects.all()
    return render( request, 'food/edit.html', {'food': food, 'categorys':categorys})

@csrf_exempt
def update(request, id):
    food = Food.objects.get(id= id)
    name = request.POST['name']
    quantity = request.POST['quantity']
    weight = request.POST['weight']
    
    name_category = request.POST['category']
    category = Category.objects.get(name= name_category)
    food.name = name
    food.quantity = quantity
    food.weight = weight
    food.category = category

    food.save()
    return redirect('/')

@csrf_exempt
def delete(request, id):
    food = Food.objects.get(id= id)
    food.delete()
    return redirect('/')

def search(request):
    name = request.GET['name']
    foodsearch = Food.objects.filter(name__contains = name)
    print(foodsearch)
    return  render(request,'food/index.html', {'foodsearch': foodsearch})