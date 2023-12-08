from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name='holi'),
    path('nos-vemos/', views.despedida, name='bye'),
    path('fecha/', views.fechaActual, name='hoy'),
    path('edades/<int:edad>/<int:anio>', views.calculaEdad, name='edad'),
    path('herencia1/', views.herencia1_html, name='herencia1_html'),
    path('herencia2/', views.herencia2_html, name='herencia2_html'),
]
