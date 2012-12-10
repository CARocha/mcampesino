from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
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
    url(r'^admin/', include(admin.site.urls)),

    #url de pruebas luego deberan ser eliminadas
    url(r'^$',direct_to_template,{'template': 'base.html'}),

)

urlpatterns += staticfiles_urlpatterns()
