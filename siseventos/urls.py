from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    
    path('usuarios/', include('usuario.urls')),  
    path('funcionarios/', include('funcionario.urls')), 
    path('equipamentos/', include('equipamento.urls')),     
]