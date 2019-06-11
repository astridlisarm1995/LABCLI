#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model


User = get_user_model()

from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage



class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'is_bioanalista',
             'is_asistente',
            'is_paciente'
        ]

        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo',
            'is_bioanalista':'Bioanalista',
            'is_asistente': 'Asistente',
            'is_paciente': 'Paciente',
        }


# usuario/forms.py
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm
)

from usuario.models import User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


from django import forms

class FormularioContacto(forms.Form):


    asunto= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Enter your asunto'}))


    usuario= forms.CharField(max_length=100, label ='E-Mail', 
                           widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))

    mensaje = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))
