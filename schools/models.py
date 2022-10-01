from django.db import models

from directors.models import Director

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    diretor = models.ForeignKey(Director, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s %s" % (
            self.name,
            self.email,
            self.phone,
            self.created_at,
            self.updated_at
        )