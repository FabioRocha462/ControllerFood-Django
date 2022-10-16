from unicodedata import category
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .models import Category

def index (request):
    categorys = Category.objects.all().order_by('name')
    return render(request,'category/index.html', {'categorys':categorys})


def create(request):
    return render(request, 'category/create.html')

@csrf_exempt
def store(request):
    name = request.POST['name']
    category = Category(name=name)
    category.save()
    return redirect('/category')

def edit(request, id):
    category = Category.objects.get(id= id)
    return render(request, 'category/edit.html', {'category': category})

@csrf_exempt
def update(request, id):
    category = Category.objects.get(id=id)
    category.name = request.POST['name']
    category.save()
    return redirect('/category')

def show(request, id):
    category = Category.objects.get(id=id)
    foods = category.food_set.all()
    return render(request, 'category/show.html',{'category': category, 'foods':foods})
    
@csrf_exempt
def delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/category')

   
    