from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __srt__(self):
        return "%s %s" % (
            self.name,
            self.email,
            self.phone,
            self.created_at,
            self.updated_at
        )