# -*- coding:utf8 -*-

from django.shortcuts import\
        get_object_or_404,\
        render_to_response,\
        redirect,\
        RequestContext
from django.core.urlresolvers import reverse
from django.http import Http404

from pricesmap.webapp.models import *
from pricesmap.webapp.forms import ItemForm

def home(request):
    types = Produit.objects.all()

    return render_to_response(
        'home.html',
        {
            'types': types
        },
        context_instance=RequestContext(request)
    )

def detail(request, type):
    if not type in [_.url_name for _ in Produit.objects.all()]:
        return Http404

    produit = Produit.objects.get(url_name=type)
    items = produit.item_set.all()
    form = ItemForm()

    return render_to_response(
        'detail.html',
        {
            'produit': produit,
            'items': items,
            'form': form
        },
        context_instance=RequestContext(request)
    )


def add(request, type):
    if request.POST:

        produit = get_object_or_404(Produit, url_name=type)

        form = ItemForm(request.POST)
        if not form.is_valid():

            item = Item()
            item.prix = form.cleaned_data['prix']
            item.latitude = form.cleaned_data['latitude']
            item.longitude = form.cleaned_data['longitude']
            item.submitter_email = form.cleaned_data['submitter_email']
            item.comment = form.cleaned_data['comment']

            item.produit = produit

            item.save()

    return redirect(reverse('detail', args=(type)))
