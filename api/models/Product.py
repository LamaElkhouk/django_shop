from django.db import models
from .Category import Category


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    date_creation = models.DateTimeField(auto_now_add=True)
    prix = models.FloatField()
    image = models.ImageField(
        upload_to='images', height_field=None, width_field=None, max_length=None)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')

# un produit peut avoir une category et une category peut appartenir à plusieurs articles
