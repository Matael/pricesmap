# -*- coding: utf8 -*-
from django.db import models
import pricesmap.settings_test as settings

class Produit(models.Model):
    """
    Représente un type de produit
    """

    name = models.CharField(max_length=200)
    description = models.TextField(
        help_text="Peut contenir du HTML pour la mise en forme. Ne sera pas vérifié lors de l'affichage (mark_safe)"
    )

    def __unicode__(self):
        return self.name


class Item(models.Model):
    """
    Représente une entrée pour un produit donné
    """

    prix = models.DecimalField(max_digits=4, decimal_places=2)
    submitter_email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    # foreign key
    produit = models.ForeignKey('Produit')

    def __unicode__(self):
        return self.produit.name+'@'+self.id
