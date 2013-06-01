# -*- coding:utf8 -*-

from django.shortcuts import\
        get_object_or_404,\
        render_to_response,\
        RequestContext

from views import *


def home(request):
    types = Produit.objects.all()

    return render_to_response(
        'home.html',
        {
            'types': types
        },
        context_instance=RequestContext(request)
    )


