from django import forms
from .models import Marca
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca 
        fields = ['marca','modelo','serial_carroceria','serial_motor','categoria','precio']
        

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Campos del formulario

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user        