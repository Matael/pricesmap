from django.forms import ModelForm

from pricesmap.webapp.models import Item

class ItemForm(ModelForm):

    class Meta:
        model = Item

        exclude = ('date', 'produit')
