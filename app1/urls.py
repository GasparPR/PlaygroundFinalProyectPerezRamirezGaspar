from django.urls import path
from . import views 

urlpatterns = [path('crear_tecnologia/', views.crear_tecnologia, name='crear_tecnologia'),
path ('index/', views.index, name='index'),
path('formulario_comentario/', views.FormularioComentario, name='formulario_comentario'),
path('login/', views.login_view, name='login'),
path('register_view/', views.register_view, name='register_view')
]