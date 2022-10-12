from django.shortcuts import render

# Create your views here.

from food.models import Food
from category.models import Category

def allfood(request):
    foods = Food.objects.all().order_by('name')
    categorys = Category.objects.all()
    return render(request, 'reports/index.html', {'foods':foods, 'categorys':categorys})

def forcategory(request):
    name = request.GET['name']
    category = Category.objects.get(name = name)
    categorys = Category.objects.all()
    foods = category.food_set.all().order_by('name')
    return render(request, 'reports/index.html', {'foods':foods, categorys:categorys})

def fordate(request):
    date = request.GET['date']
    categorys = Category.objects.all()
    foods = Food.objects.filter(validity__lte = date)
    return render(request, 'reports/index.html', {'foods':foods, categorys:categorys})
