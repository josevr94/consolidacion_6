from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home,name='home'),
    path('vehiculo/add/',views.formulario,name='formulario'),
    path('vehiculo/lista',views.lista_autos,name='lista'),
    path('registro/',views.registro,name='registro')
    
    
]