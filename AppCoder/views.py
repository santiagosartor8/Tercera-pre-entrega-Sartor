from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from AppCoder.models import Autor, Editorial, Resena
from .forms import AutorForm, ResenaForm, EditorialForm
from django.views import View

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'listar_autores.html', {'autores': autores})

def listar_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'listar_editoriales.html', {'editoriales': editoriales})

def listar_resenas(request):
    resenas = Resena.objects.all()
    return render(request, 'listar_resenas.html', {'resenas': resenas})

def detalle_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    return render(request, 'detalle_autor.html', {'autor': autor})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()

    return render(request, 'crear_autor.html', {'form': form})

def crear_resena(request):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_resenas')
    else:
        form = ResenaForm()

    return render(request, 'crear_resena.html', {'form': form})

def crear_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_editoriales')
    else:
        form = EditorialForm()

    return render(request, 'crear_editorial.html', {'form': form})

class PaginaInicioView(View):
    template_name = 'pagina_inicio.html'

    def get(self, request):
        return render(request, self.template_name)