from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    phone_number = models.CharField(max_length=15, default=1)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='main_app/static/uploads', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'animal_id': self.id})
    
class Comment(models.Model):
    blog_post = models.ForeignKey(Animal, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog_post.name} - {self.title}"

class VeterinaryHospital(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    location_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='main_app/static/uploads', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('veterinary_detail', kwargs={'veterinary_id': self.id})