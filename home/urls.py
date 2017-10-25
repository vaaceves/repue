from django.conf.urls import url
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),  # url inicio
    url(r'^about/', views.about, name='about'),  # url acerca de
    url(r'^all/$', views.all_content, name='all'),  # url para lista de todos los contenidos
    url(r'^(?P<slug_content>[-\w\d]+)/$', views.content_detail, name='content-detail'), # url para contenido en especifico con sus detalles
    # url para contenido en filtrado por tematica
    url(r'^tematica/(?P<slug_tematica>[\w\-]+)/$', views.vista_tematica, name='content-by-tematica'),
    url(r'^pais/(?P<slug_pais>[\w\-]+)/$', views.vista_pais, name='content-by-pais'),
    # url para vistas genericas
    url(r'^new/publicar$', views.ContentCreateView.as_view(), name='publicar'),  # publicar contenido
    url(r'^(?P<slug>[-\w\d]+)/actualizar/$', views.ContentUpdateView.as_view(), name='actualizar'),
    # actualizar contenido
    url(r'^(?P<slug>[-\w\d]+)/eliminar/$', views.ContentDeleteView.as_view(), name="eliminar"),  # eliminar contenido
]
