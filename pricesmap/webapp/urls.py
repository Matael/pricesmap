from django.conf.urls import patterns, include, url

from django.views.generic.base import TemplateView

class AboutView(TemplateView):

    template_name = "about.html"
urlpatterns = patterns('pricesmap.webapp.views',
    url(r'^product/(?P<type>\w+)/?$', 'detail', name='detail'),
    url(r'^product/(?P<type>\w+)/add/?$', 'add', name='add'),
)


urlpatterns += patterns('',
    url(r'^about/?$', AboutView.as_view(), name="about")
)

