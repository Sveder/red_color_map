from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'theapp.views.home', name='home'),
    
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

    #API urls:
    url(r'^api/latest$', 'theapp.api.latest', name='latest'),
    url(r'^api/latest/debug$', 'theapp.api.latest_debug', name='latest_debug'),

    url(r'^api/area_error$', 'theapp.api.area_error', name='area_error'),

    # url(r'^red_color_map/', include('red_color_map.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
