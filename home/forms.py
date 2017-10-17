#importamos api forms desde django
from django import forms
from django.utils.text import slugify
from django.forms import ModelForm

#importamos los modelos
from models import Contenido

class FormCrearContenido(forms.ModelForm):
    """Clase para crear un formulario
    a partir de un modelo definido"""
    class Meta:
        """clase interna donde se define:
        - de que modelo es el form a contruir asignado a la variable model
        - cuales campor tendra el formulario, variable fields"""
        model = Contenido
        fields = [
            'titulo', 'tipo', 'descripcion', 'autores', 'anoPublicacion', 'pais',
            'evento', 'libro', 'tematica', 'descarga', 'video', 'portada', 'issuu', 'slug',
                  ]

    def save(self):
        def save(self):
            instance = super(AddForm, self).save(commit=False)
            instance.slug = slugify(instance.title)
            instance.save()

            return instance
