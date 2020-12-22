from django.shortcuts import render, redirect
from .models import Libro
from .forms import ContactoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import viewsets
from .serializers import LibroSerializers

# Create your views here.

def home(request):
    libros = Libro.objects.all()
    data = {
        'libros': libros
    }
       
    return render(request, 'web/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
           formulario.save()
           data["mensaje"] = "contacto guardado"
        else:
           data["form"] = formulario

    return render(request, 'web/contacto.html', data)

def index(request):
    return render(request, 'web/index.html')


def compra(request):
    return render(request, 'web/compra.html')    


def registro(request):


    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
            password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def error_facebook(request):
    return render(request, 'registration/error_facebook.html')



#se encargara de tomar los datos y guaradarlos , transformar los datos a json
class LibroViewset(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    #Para comvertirlos a serializador
    serializer_class = LibroSerializers




