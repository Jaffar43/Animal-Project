from django.shortcuts import render, redirect
from .models import Animal, Comment,VeterinaryHospital
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    animals = Animal.objects.all()
    return render(request, 'home.html', { 'animals': animals })

def about(request):
    return render(request, 'about.html')

@login_required
def animals_index(request):
    animals = Animal.objects.filter(user=request.user)
    # animals = Animal.objects.all()
    return render(request, 'animals/index.html', { 'animals': animals })

@login_required
def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animals/detail.html', {'animal': animal})

class AnimalCreate(LoginRequiredMixin, CreateView):
    model = Animal
    fields = ['name', 'species', 'breed', 'price', 'description', 'image']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AnimalUpdate(LoginRequiredMixin, UpdateView):
    model = Animal
    fields = ['species', 'breed', 'price', 'description']

class AnimalDelete(LoginRequiredMixin, DeleteView):
    model = Animal
    success_url = '/animals/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def add_comment(request, animal_id):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            title = request.POST["title"]
            body = request.POST["body"]
            commented_post = Animal.objects.get(id=animal_id)
            new_comment = Comment.objects.create(user=current_user, title=title, body=body, blog_post=commented_post)
            new_comment.save()
            print("Comment Created!")
            return redirect('detail', animal_id=commented_post.id)
        else:
            return render(request, 'animals/add_comment.html')
    else:
        print("Not logged in")
        return redirect('home')


def veterinary_index(request):
    veterinarys = VeterinaryHospital.objects.all()
    return render(request, 'veterinary/veterinary_index.html', { 'veterinarys': veterinarys })

@login_required
def my_veterinary(request):
    veterinarys = VeterinaryHospital.objects.filter(user=request.user)
    return render(request, 'veterinary/my_veterinary.html', { 'veterinarys': veterinarys })

@login_required
def veterinary_detail(request, veterinary_id):
    veterinary = VeterinaryHospital.objects.get(id=veterinary_id)
    return render(request, 'veterinary/veterinary_detail.html', {'veterinary': veterinary})

class VeterinaryHospitalCreate(LoginRequiredMixin, CreateView):
    model = VeterinaryHospital
    fields = ['name', 'email', 'phone_number', 'address', 'location_link']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VeterinaryHospitalUpdate(LoginRequiredMixin, UpdateView):
    model = VeterinaryHospital
    fields = ['email', 'phone_number', 'address', 'location_link']

class VeterinaryHospitalDelete(LoginRequiredMixin, DeleteView):
    model = VeterinaryHospital
    success_url = '/veterinarys/'