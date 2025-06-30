from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animals_index, name='index'),
    path('animals/<int:animal_id>/', views.animal_detail, name='detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animals_create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete'),

    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/logout/', views.logout_view, name='logout'),

    path('add_comment/<int:animal_id>/', views.add_comment, name='add_comment'),

    path('veterinarys/', views.veterinary_index, name='veterinary_index'),
    path('my_veterinarys/', views.my_veterinary, name='my_veterinary'),
    path('veterinarys/<int:veterinary_id>', views.veterinary_detail, name='veterinary_detail'),
    path('veterinarys/create/', views.VeterinaryHospitalCreate.as_view(), name='veterinarys_create'),
    path('veterinarys/<int:pk>/update/', views.VeterinaryHospitalUpdate.as_view(), name='veterinarys_update'),
    path('veterinarys/<int:pk>/delete/', views.VeterinaryHospitalDelete.as_view(), name='veterinarys_delete'),

    path('search/', views.search, name='search'),
]