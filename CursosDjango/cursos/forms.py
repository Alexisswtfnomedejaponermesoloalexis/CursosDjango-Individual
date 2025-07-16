from django import forms
from .models import ComentarioContacto, Cursos
from django.forms import ModelForm

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje', 'curso'] 
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tu mensaje'}),
            'curso': forms.Select(attrs={'class': 'form-control'}), 
        }
        

class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = '__all__'
        widgets = {
            'codCurso': forms.TextInput(attrs={
                'placeholder': 'Ej: CURS01',
                'class': 'form-control'
            }),
            'nameCurso': forms.TextInput(attrs={
                'placeholder': 'Ej: Álgebra Lineal',
                'class': 'form-control'
            }),
            'cupo_maximo': forms.NumberInput(attrs={
                'placeholder': 'Ej: 30',
                'class': 'form-control'
            }),
            'costo': forms.NumberInput(attrs={
                'placeholder': 'Ej: 1500.00',
                'class': 'form-control',
                'step': '0.01'
            }),
            'contacto': forms.EmailInput(attrs={
                'placeholder': 'Ej: contacto@universidad.edu',
                'class': 'form-control'
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'codCurso': "Código del Curso",
            'nameCurso': "Nombre del Curso",
            'cupo_maximo': "Cupo Máximo",
            'turnoCurso': "Turno",
            'disponible': "¿Disponible?",
            'costo': "Costo ($)",
            'contacto': "Email de Contacto",
            'imagen': "Imagen del Curso"
        }