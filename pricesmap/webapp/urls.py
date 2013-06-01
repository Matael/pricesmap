from django.conf.urls import patterns, include, url

urlpatterns = patterns('pricesmap.webapp.views',
    url(r'^$', 'home', name='home'),
)



