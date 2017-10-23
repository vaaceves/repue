"""repue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.conf.urls import url
from django.contrib import admin
from django.views.debug import default_urlconf
from django.conf import settings
from django.conf.urls.static import static
from home import views
from django.conf.urls import include
=======
from django.conf.urls import url, include
from django.contrib import admin
from home import views
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> origin/master

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^home/', include('home.urls')),
    url(r'^busqueda/$', views.SearchSubmitView.as_view(), name='search_submit'),
    # above maps any URLs starting
    # with home/ to be handled by
    # the home application
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    url(r'^about/', views.about, name='about'),
    url(r'^home/', include('home.urls')),
    # above maps any URLs starting
    # with home/ to be handled by
    # the home application
]
>>>>>>> origin/master
