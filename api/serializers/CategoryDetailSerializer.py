from api.models import Category, Product
from rest_framework import serializers
from api.serializers import ProductSerializer


class ProductForCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'nom', 'prix']


class CategoryDetailSerializer(serializers.ModelSerializer):
    # En utilisant un `SerializerMethodField', il est nécessaire d'écrire une méthode
    # nommée 'get_XXX' où XXX est le nom de l'attribut, ici 'products'
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'nom', 'description', 'products']

    def get_products(self, instance):
        # Le paramètre 'instance' est l'instance de la catégorie consultée.
        # Dans le cas d'une liste, cette méthode est appelée autant de fois qu'il y a
        # d'entités dans la liste

        # On applique le filtre sur notre queryset pour n'avoir que les produits actifs
        queryset = instance.products.filter(active=True).order_by('-prix')
        # Le serializer est créé avec le queryset défini et toujours défini en tant que many=True
        serializer = ProductForCategorySerializer(queryset, many=True)
        # la propriété '.data' est le rendu de notre serializer que nous retournons ici
        return serializer.data
