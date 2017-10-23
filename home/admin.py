from django.contrib import admin

<<<<<<< HEAD
from models import Autor, Evento, Tematica, Libro, Pais, Contenido


# AdminCustom
class PostModelAdminAutor(admin.ModelAdmin):
    list_display = ["apellido", "nombre", "paisResidencia", "institucion", "email"]
    search_fields = ["nombre", "apellido"]

    class Meta:
        model = Autor


class PostModelAdminContenido(admin.ModelAdmin):
    list_display = ["titulo", "tematica", "anoPublicacion", "tipo", "timestamp"]
    search_fields = ["titulo", "anoPublicacion", "autores__nombre", "autores__apellido"]

    class Meta:
        model = Contenido


class PostModelAdminLibro(admin.ModelAdmin):
    list_display = ["titulo", "edicion", "anoPublicacion"]

    class Meta:
        model = Libro
=======
from models import Autor, Evento, Tematica, Libro, Pais, Clasificacion, Contenido
#AdminCustom
class PostModelAdminAutor(admin.ModelAdmin):
    list_display = ["apellido", "nombre", "paisResidencia", "institucion", "email"]
    search_fields = ["nombre","apellido"]
    class Meta:
        model = Autor

class PostModelAdminContenido(admin.ModelAdmin):
     list_display = ["titulo", "tematica", "anoPublicacion", "tipo", "timestamp"]
     search_fields = ["titulo","anoPublicacion", "autores__nombre", "autores__apellido"]
     class Meta:
         model = Contenido

class PostModelAdminLibro(admin.ModelAdmin):
     list_display = ["titulo", "edicion", "anoPublicacion"]
     class Meta:
         model = Libro

>>>>>>> origin/master


# Register your models here.
admin.site.register(Autor, PostModelAdminAutor)
admin.site.register(Evento)
admin.site.register(Tematica)
admin.site.register(Contenido, PostModelAdminContenido)
<<<<<<< HEAD
=======
admin.site.register(Clasificacion)
>>>>>>> origin/master
admin.site.register(Libro, PostModelAdminLibro)
admin.site.register(Pais)
