from django.db import models


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
