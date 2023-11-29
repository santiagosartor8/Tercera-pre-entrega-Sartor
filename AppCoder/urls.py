from django.contrib import admin
from django.urls import path
from .views import PaginaInicioView, listar_autores, listar_editoriales, listar_resenas, detalle_autor, crear_autor, crear_editorial, crear_resena

urlpatterns = [
    path('', PaginaInicioView.as_view(), name='pagina_inicio'),
    path('autores/', listar_autores, name='listar_autores'),
    path('autores/<int:autor_id>/', detalle_autor, name='detalle_autor'),
    path('editoriales/', listar_editoriales, name='listar_editoriales'),
    path('resenas/', listar_resenas, name='listar_resenas'),
    path('autores/crear/', crear_autor, name='crear_autor'),
    path('editoriales/crear/', crear_editorial, name='crear_editorial'),
    path('resenas/crear/', crear_resena, name='crear_resena'),
]

