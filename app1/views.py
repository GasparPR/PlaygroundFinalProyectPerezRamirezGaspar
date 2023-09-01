from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def crear_tecnologia(request):
    if request.method == 'POST':
        form = FormularioTecnologia(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Formulario válido, datos guardados en la base de datos")
            return redirect('index.html')  
    else:
        form = FormularioTecnologia()
        
    
    return render(request, 'crear_tecnologia.html', {'form': form})

def FormularioComentario(request):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.tecnologia = tecnmologia
            comentario.autor = request.user
            comentario.save()
            return redirect('index.html', pk=pk)  
    else:
        form = ComentarioForm()
    
    return render(request, 'app1/agregar_comentario.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("creado correctamente")
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register_view.html', {'form': form})
