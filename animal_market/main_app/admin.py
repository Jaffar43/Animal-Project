from django.contrib import admin
from .models import Animal, Comment

# Register your models here.
admin.site.register(Animal)
admin.site.register(Comment)