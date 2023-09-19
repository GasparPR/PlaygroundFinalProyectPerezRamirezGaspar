from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


def crear_tecnologia(request):
    if request.method == 'POST':
        form = FormularioTecnologia(request.POST, request.FILES)
        if form.is_valid():
            # Validar y convertir campos a enteros
            year = int(request.POST['year'])
            precio = int(request.POST['precio'])
            telefono_contacto = int(request.POST['telefonoContacto'])
            
            # Asignar los valores convertidos de nuevo al formulario
            form.cleaned_data['year'] = year
            form.cleaned_data['precio'] = precio
            form.cleaned_data['telefonoContacto'] = telefono_contacto
            
            # Guardar el formulario
            form.save()
            print("Formulario válido, datos guardados en la base de datos")
            return redirect('index')  # Corregido: 'index.html' a 'index'
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


