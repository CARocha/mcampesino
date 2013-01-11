from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from settings import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mcampesino.views.home', name='home'),
    # url(r'^mcampesino/', include('mcampesino.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include('movimientos.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    #url de pruebas luego deberan ser eliminadas
    #url(r'^$',direct_to_template,{'template': 'index.html'}),
    #url(r'^explora/$',direct_to_template,{'template': 'explora.html'}),
    #url(r'^explora/mercado/$',direct_to_template,{'template': 'mercado.html'}),

)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )
