from rest_framework.viewsets import ModelViewSet
from api.serializers import CategorySerializer
from api.models import Category


class CategoryViewset(ModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all().filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        return queryset
        # return Category.objects.all()
