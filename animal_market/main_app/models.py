from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='main_app/static/uploads', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'animal_id': self.id})