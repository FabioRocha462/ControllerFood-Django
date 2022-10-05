from django.db import models

from category.models import Category
from schools.models import School

# Create your models here.

class Food(models.Model):
   name = models.CharField(max_length=255)
   validity = models.DateField()
   quantity = models.IntegerField(null=True)
   weight = models.FloatField(null = True)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   school = models.ManyToManyField(School)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   def __str__(self):
    return (self.name)