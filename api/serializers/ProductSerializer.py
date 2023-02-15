from api.models import Product, Category
from rest_framework import serializers


class CategorySerializerForProduct(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'nom']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializerForProduct()

    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    # La validation d’un champ unique se fait en écrivant la méthode validate_XXX
    # où XXX  est le nom du champ. Dans notre cas, validate_name  :

    def validate_nom(self, value):
        # Nous vérifions que la catégorie existe
        if Product.objects.filter(nom=value).exists():
            # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Ce produit existe déjà ...')
        return value

    def validate(self, data):
        # Effectuons le contrôle sur la présence du nom dans la description
        if data['nom'] not in data['description']:
            # Levons une ValidationError si ça n'est pas le cas
            raise serializers.ValidationError(
                'Le nom doit etre présent dans la description..')
        return data
