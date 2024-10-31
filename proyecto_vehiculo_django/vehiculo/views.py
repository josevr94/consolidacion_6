from django.shortcuts import render, redirect
from .models import Marca
from .forms import MarcaForm, CustomUserCreationForm
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required


def registro(request):
    # Creamos el contexto inicial con el formulario de registro
    data = {
        'form': CustomUserCreationForm()
    }

    # Comprobamos si la solicitud es de tipo POST (es decir, si se envió el formulario)
    if request.method == 'POST':
        # Creamos una instancia del formulario con los datos enviados
        formulario = CustomUserCreationForm(data=request.POST)
        
        # Validamos el formulario
        if formulario.is_valid():
            # Guardamos el usuario en la base de datos
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            
            # Autenticamos al usuario recién creado
            user = authenticate(username=username, password=password)
            
            # Si la autenticación es exitosa, asignamos permisos
            if user is not None:
                # Obtenemos el tipo de contenido (content type) del modelo BoardsModel
                content_type = ContentType.objects.get_for_model(Marca)
                
                # Obtenemos el permiso 'visualizar_lista' asociado a este tipo de contenido
                visualizar_lista = Permission.objects.get(
                    codename='visualizar_lista',
                    content_type=content_type
                )
                
                # Asignamos el permiso al usuario
                user.user_permissions.add(visualizar_lista)
                
                # Iniciamos sesión automáticamente para el nuevo usuario
                login(request, user)
                
                # Mostramos un mensaje de éxito
                messages.success(request, "Te has registrado correctamente.")
                
                # Redirigimos al menú principal
                return redirect('home')
        
        # Si el formulario no es válido, lo agregamos al contexto para mostrar los errores
        data['form'] = formulario

    # Renderizamos el formulario de registro en la plantilla
    return render(request, 'registration/register.html', data)





def home(request):
    return render(request,'vehiculo/index.html')

@permission_required('vehiculo.add_marca')
def formulario(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Vehiculo agregado exitosamente')
            return  redirect('lista')
    else:
        form = MarcaForm()
    return render(request,'vehiculo/formulario.html',{'form':form})        
        
        
@permission_required('vehiculo.visualizar_lista')        
def lista_autos(request):
    listas = Marca.objects.all()
    
    return render(request,'vehiculo/lista.html',{'listas': listas})
            
            
                 