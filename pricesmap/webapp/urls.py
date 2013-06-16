from django.conf.urls import patterns, include, url

urlpatterns = patterns('pricesmap.webapp.views',
    url(r'^product/(?P<type>\w+)/?', 'detail', name='detail'),
    url(r'^product/(?P<type>\w+)/add/?', 'add', name='add'),
)



