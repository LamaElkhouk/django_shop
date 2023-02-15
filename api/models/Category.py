from django.db import models, transaction


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    @transaction.atomic
    def disable(self):
        if self.active is False:
            # Ne faisons rien si la catégorie est déjà désactivée
            return
        self.active = False
        self.save()
        self.products.update(active=False)

    @transaction.atomic
    def unable(self):
        if self.active is True:
            # Ne faisons rien si la catégorie est déjà désactivée
            return
        self.active = True
        self.save()
        self.products.update(active=True)
