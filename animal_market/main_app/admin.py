from django.contrib import admin
from .models import Animal, Comment, VeterinaryHospital, Product

# Register your models here.
admin.site.register(Animal)
admin.site.register(Comment)
admin.site.register(VeterinaryHospital)
admin.site.register(Product)

