from __future__ import unicode_literals
from django.template import defaultfilters
from django.db import models

# Create your models here.

# ______________________________________________________________________
class Clasificacion(models.Model):
    tipo_de_contenido = models.CharField(max_length=15)

    def __unicode__(self):
        return self.tipo_de_contenido

    # .....
    class Meta:
        verbose_name_plural = 'Clasificaciones'

# ______________________________________________________________________
class Pais(models.Model):
    pais = models.CharField(max_length=15)

    def __unicode__(self):
        return self.pais

    # .....
    class Meta:
        verbose_name_plural = 'Paises'


# ______________________________________________________________________
class Tematica(models.Model):
   nombreTematica = models.CharField(max_length=100)
   slug = models.SlugField(unique=True, null=False, blank=False)

   def save(self, *args, **kwargs):
       if not self.id:
           self.slug = defaultfilters.slugify(self.nombreTematica)
           super(Tematica, self).save(*args, **kwargs)


   def __unicode__(self):  # __str__ para python 3
      return self.nombreTematica


# ______________________________________________________________________
class Autor(models.Model):
    '''Un autor tiene un nombre, un apellido y un email'''
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    puesto = models.CharField(max_length=150)
    institucion = models.CharField(max_length=100)
    paisResidencia = models.ForeignKey(Pais)
    cv = models.URLField()
    email = models.EmailField(blank=True)  # La BBDD aceptara valores vacios para este atributo
    tematicas = models.ManyToManyField(Tematica)
    def __unicode__(self):  # __str__ para python 3
        cadena = "%s %s" % (self.nombre, self.apellido)
        return cadena

    # .....
    class Meta:
        verbose_name_plural = 'Autores'


# ______________________________________________________________________
class Evento(models.Model):
    evento = models.CharField(max_length=150)

    def __unicode__(self):  # __str__ para python 3
        return self.evento


# ______________________________________________________________________
class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    edicion = models.CharField(max_length=150)
    anoPublicacion = models.PositiveSmallIntegerField(null=False, blank=False)
    portada = models.ImageField(
        upload_to='portadas/')  #carpeta llamada portadas, donde guardara las imagenes de portadas de libros, al final la imagen tendra que cargarse en: media/portadas/
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = defaultfilters.slugify(self.titulo)
            super(Libro, self).save(*args, **kwargs)

    def __unicode__(self):  # __str__ para python 3
        return self.titulo


# ______________________________________________________________________
class Contenido(models.Model):
    '''un material tiene Titulo,Descripcion,Ano de Publicacion,Tematica,Evento,Pais,Video, AUTOR, etc'''
    autores = models.ManyToManyField(Autor)
    tematica = models.ForeignKey(Tematica)
    titulo = models.CharField(max_length=200)  # el atributo nombre tendra maximo 150 caracteres
    slug = models.SlugField(max_length=80, default="textoURL-separado-por-guiones")
    descripcion = models.TextField(max_length=350, blank=True)
    tipo = models.ForeignKey(Clasificacion)
    evento = models.ForeignKey(Evento)
    libro = models.ForeignKey(Libro)
    anoPublicacion = models.PositiveIntegerField(null=True)
    pais = models.ManyToManyField(Pais)
    timestamp = models.DateTimeField(auto_now=True)#fecha en que se publico
    issuu = models.TextField(max_length=250, default="codigo para insertar issuu (Embeded)")
    portada = models.ImageField(
        upload_to='portadas/')  #carpeta llamada portadas, donde guardara las imagenes de portadas de libros, al final la imagen tendra que cargarse en: media/portadas/
    descarga = models.URLField(default="http://www.redue-alcue.org")
    video = models.URLField(default="http://www.youtube.com")
    destacar = models.BooleanField(default=False)

    def __unicode__(self):  # __str__ para python 3
        return self.titulo




