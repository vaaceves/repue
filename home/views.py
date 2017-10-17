from django.shortcuts import render
from models import Autor, Evento, Tematica, Libro, Pais, Clasificacion, Contenido
#importamos las vistas genericas de django, para crear, actualizar y eliminar
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from forms import FormCrearContenido
from django.core.urlresolvers import reverse_lazy
from django.template import defaultfilters
from django.http import HttpResponse

# Create your views here.


def index(request):
    # Construct a dictionary to pass to template engine as it context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    all_content = Contenido.objects.all().order_by('-id')[:3]  # traemos todos los contenidos
    all_tematicas = Tematica.objects.all()#para la navbar, muestra todas las tematicas para enlace
    context_dict = {
        'boldmessage' : "Bienvenidos!",
        'content_list': all_content,
        'tematica_list' : all_tematicas
    }

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'home/index.html', context=context_dict)
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
    }
    return render(request, 'home/all.html', context)



#----------------------------------------------------
def content_detail(request, slug):
    #mostrara detalles de cada contenido en especifico
    content = Contenido.objects.get(slug=slug)#traemos los detalles
    all_tematicas = Tematica.objects.all()  # para la navbar, muestra todas las tematicas para enlace
    context = {
        'this_content': content,
        'tematica_list': all_tematicas
    } #this_content = a un contenido en especifico a mostrar
    return render(request, 'home/contenido.html', context)


# __________________________________________
def vista_tematica(request, slug_tematica):
    tematicas = Tematica.objects.all()
    context_dict = {
        'tematicas': tematicas,
    }

    query = request.GET.get("q")

    try:
        tematica = Tematica.objects.get(slug=slug_tematica)
        contenidos = Contenido.objects.filter(tematica=tematica)
        if query:
            contenidos = Contenido.objects.filter(compania__icontains=query)
        context_dict['tematica'] = tematica
        context_dict['tematicas'] = tematicas
        context_dict['contenidos'] = contenidos

    except Tematica.DoesNotExist:
        context_dict['tematica'] = None
        context_dict['contenidos'] = None
        context_dict['tematicas'] = tematicas

    return render(request, 'dir/tematica.html', context_dict)



#----------------------------------------------------
#vistas genericas
#----------------------------------------------------
class ContentCreateView(CreateView):
    """con esta vista generica, tenemos la logica
       para agregar nuevo contenido"""
    model = Contenido
    #caracteristicas especiales para el form de crear
    form_class = FormCrearContenido
    template_name = 'home/vista_contenido.html'

#----------------------------------------------------
class ContentUpdateView(UpdateView):
    #nos permite actualizar un contenido en especifico
    model = Contenido
    form_class = FormCrearContenido
    template_name = 'home/vista_contenido.html'

#----------------------------------------------------
class ContentDeleteView(DeleteView):
    #nos permite eliminar un contenido en especifico
    model = Contenido
    success_url = reverse_lazy('home:index')
















