from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

from pricesmap.webapp.views import home


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    # for everything else, load url from webapp.urls
    url(r'^pm/', include('pricesmap.webapp.urls')),
    url(r'^/?$', home , name='home'),
)

