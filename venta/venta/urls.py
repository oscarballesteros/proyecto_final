from django.conf.urls import patterns, include, url
from apps.principal import views
#from venta.apps.principal.views import hola
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'venta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('venta.apps.principal.urls')),
    #url(r'^preferencia/',preferencias),
    #url(r'^$',hola),
    #url(r'^$')
)
