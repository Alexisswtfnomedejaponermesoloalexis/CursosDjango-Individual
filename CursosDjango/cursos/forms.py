from django import forms
from .models import ComentarioContacto
from django.forms import ModelForm

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario','mensaje']