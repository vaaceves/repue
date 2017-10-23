from django.shortcuts import render
<<<<<<< HEAD

from models import *
# importamos las vistas genericas de django, para crear, actualizar y eliminar
=======
from models import Autor, Evento, Tematica, Libro, Pais, Clasificacion, Contenido
#importamos las vistas genericas de django, para crear, actualizar y eliminar
>>>>>>> origin/master
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from forms import FormCrearContenido
from django.core.urlresolvers import reverse_lazy
from django.template import defaultfilters
from django.http import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.template import loader
from django.http import HttpResponse
from django.views.generic.base import View
from django.db.models import Q

=======
>>>>>>> origin/master

# Create your views here.


def index(request):
    # Construct a dictionary to pass to template engine as it context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    all_content = Contenido.objects.all().order_by('-id')[:3]  # traemos todos los contenidos
<<<<<<< HEAD
    all_tematicas = Tematica.objects.all()  # para la navbar, muestra todas las tematicas para enlace
    paises = Pais.objects.all()
    context_dict = {
        'boldmessage': "Bienvenidos!",
        'content_list': all_content,
        'tematica_list': all_tematicas,
        'pais_list': paises,
=======
    all_tematicas = Tematica.objects.all()#para la navbar, muestra todas las tematicas para enlace
    context_dict = {
        'boldmessage' : "Bienvenidos!",
        'content_list': all_content,
        'tematica_list' : all_tematicas
>>>>>>> origin/master
    }

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'home/index.html', context=context_dict)
<<<<<<< HEAD
    # return HttpResponse("Repositorio Universidad-Empresa <br> - <a href='/repositorio/about/'> Acerca de </a>")


# __________________________________________
# busqueda
# __________________________________________
class SearchSubmitView(View):
    template = 'home/search-submit.html'
    response_message = 'Resultados de Busqueda:'

    def post(self, request):
        template = loader.get_template(self.template)
        query = request.POST.get('search', '')

        contenidos = Contenido.objects.filter(titulo__icontains=query)
        tematicas = Tematica.objects.all()
        paises = Pais.objects.all()

        context = {'title': self.response_message, 'query': query, 'contenidos': contenidos,
                   'tematica_list': tematicas, 'pais_list': paises, }

        rendered_template = template.render(context, request)
        return HttpResponse(rendered_template, content_type='text/html')


# ----------------------------------------------------
def about(request):
    all_tematicas = Tematica.objects.all()  # para la navbar, muestra todas las tematicas para enlace
    paises = Pais.objects.all()
    context_dict = {
        'tematica_list': all_tematicas,
        'pais_list': paises,
    }
    return render(request, 'home/about.html', context=context_dict)
    # return HttpResponse("Acerca del Repositorio Universidad-Empresa <br> <a href='/home/'> Regresar </a> ")


# ----------------------------------------------------
def all_content(request):
    # hara la gestion para mostrar todas las publicaciones
    all_content = Contenido.objects.all().order_by('-id')  # traemos todos los contenidos
    all_tematicas = Tematica.objects.all()  # para la navbar, muestra todas las tematicas para enlace
    # first_author = Contenido.autores.all()
    paises = Pais.objects.all()
    context = {
        'content_list': all_content,
        'tematica_list': all_tematicas,
        'pais_list': paises,
        # 'primer_autor': first_author
=======
    #return HttpResponse("Repositorio Universidad-Empresa <br> - <a href='/repositorio/about/'> Acerca de </a>")



#----------------------------------------------------
def about(request):
    all_tematicas = Tematica.objects.all()  # para la navbar, muestra todas las tematicas para enlace
    context_dict = {
        'tematica_list': all_tematicas
    }
    return render(request, 'home/about.html',context=context_dict)
    #return HttpResponse("Acerca del Repositorio Universidad-Empresa <br> <a href='/home/'> Regresar </a> ")



#----------------------------------------------------
def all_content(request):
    #hara la gestion para mostrar todas las publicaciones
    all_content = Contenido.objects.all().order_by('-id')#traemos todos los contenidos
    all_tematicas = Tematica.objects.all()  # para la navbar, muestra todas las tematicas para enlace
    #first_author = Contenido.autores.all()
    context = {
        'content_list':all_content,
        'tematica_list': all_tematicas
        #'primer_autor': first_author
>>>>>>> origin/master
    }
    return render(request, 'home/all.html', context)


<<<<<<< HEAD
# ----------------------------------------------------
def content_detail(request, slug_content):
    # mostrara detalles de cada contenido en especifico
    all_tematicas = Tematica.objects.all()  # para la navbar, muestra todas las tematicas para enlace
    paises = Pais.objects.all()
    context = {
        'tematica_list': all_tematicas,
        'pais_list': paises,
    }  # this_content = a un contenido en especifico a mostrar

    try:
        contenido = Contenido.objects.get(slug=slug_content)  # traemos los detalles
        context['this_content'] = contenido

    except Contenido.DoesNotExist:
        context['this_content'] = None

=======

#----------------------------------------------------
def content_detail(request, slug):
    #mostrara detalles de cada contenido en especifico
    content = Contenido.objects.get(slug=slug)#traemos los detalles
    all_tematicas = Tematica.objects.all()  # para la navbar, muestra todas las tematicas para enlace
    context = {
        'this_content': content,
        'tematica_list': all_tematicas
    } #this_content = a un contenido en especifico a mostrar
>>>>>>> origin/master
    return render(request, 'home/contenido.html', context)


# __________________________________________
def vista_tematica(request, slug_tematica):
    tematicas = Tematica.objects.all()
<<<<<<< HEAD
    paises = Pais.objects.all()
    context_dict = {
        'tematica_list': tematicas,
        'pais_list': paises,
=======
    context_dict = {
        'tematicas': tematicas,
>>>>>>> origin/master
    }

    query = request.GET.get("q")

    try:
        tematica = Tematica.objects.get(slug=slug_tematica)
        contenidos = Contenido.objects.filter(tematica=tematica)
        if query:
            contenidos = Contenido.objects.filter(compania__icontains=query)
        context_dict['tematica'] = tematica
<<<<<<< HEAD
=======
        context_dict['tematicas'] = tematicas
>>>>>>> origin/master
        context_dict['contenidos'] = contenidos

    except Tematica.DoesNotExist:
        context_dict['tematica'] = None
        context_dict['contenidos'] = None
<<<<<<< HEAD

    return render(request, 'home/tematica.html', context_dict)


# __________________________________________
def vista_pais(request, slug_pais):
    tematicas = Tematica.objects.all()
    paises = Pais.objects.all()
    context_dict = {
        'tematica_list': tematicas,
        'pais_list': paises,
    }

    query = request.GET.get("q")

    try:
        pais = Pais.objects.get(slug=slug_pais)
        contenidos = Contenido.objects.filter(pais=pais)
        if query:
            contenidos = Contenido.objects.filter(compania__icontains=query)
        context_dict['pais'] = pais
        context_dict['contenidos'] = contenidos

    except Tematica.DoesNotExist:
        context_dict['pais'] = None
        context_dict['contenidos'] = None

    return render(request, 'home/pais.html', context_dict)


# ----------------------------------------------------
# vistas genericas
# ----------------------------------------------------
=======
        context_dict['tematicas'] = tematicas

    return render(request, 'dir/tematica.html', context_dict)



#----------------------------------------------------
#vistas genericas
#----------------------------------------------------
>>>>>>> origin/master
class ContentCreateView(CreateView):
    """con esta vista generica, tenemos la logica
       para agregar nuevo contenido"""
    model = Contenido
<<<<<<< HEAD
    # caracteristicas especiales para el form de crear
    form_class = FormCrearContenido
    template_name = 'home/vista_contenido.html'


# ----------------------------------------------------
class ContentUpdateView(UpdateView):
    # nos permite actualizar un contenido en especifico
=======
    #caracteristicas especiales para el form de crear
    form_class = FormCrearContenido
    template_name = 'home/vista_contenido.html'

#----------------------------------------------------
class ContentUpdateView(UpdateView):
    #nos permite actualizar un contenido en especifico
>>>>>>> origin/master
    model = Contenido
    form_class = FormCrearContenido
    template_name = 'home/vista_contenido.html'

<<<<<<< HEAD

# ----------------------------------------------------
class ContentDeleteView(DeleteView):
    # nos permite eliminar un contenido en especifico
    model = Contenido
    success_url = reverse_lazy('home:index')
=======
#----------------------------------------------------
class ContentDeleteView(DeleteView):
    #nos permite eliminar un contenido en especifico
    model = Contenido
    success_url = reverse_lazy('home:index')
















>>>>>>> origin/master
