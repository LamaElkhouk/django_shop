from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers import CategoryListSerializer, CategoryDetailSerializer
from api.models import Category


class CategoryViewset(ModelViewSet):

    serializer_class = CategoryListSerializer  # par défaut

    # Ajoutons un attribut de classe qui nous permet de définir notre serializer de détail
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        return queryset
        # return Category.objects.all()

    def get_serializer_class(self):
        # Si l'action demandée est retrieve nous retournons le serializer de détail
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    @action(detail=True, methods=['post'], url_path='desactiver')
    def disable(self, request, pk):
        category = self.get_object()
        category.active = False
        category.save()
        category.products.update(active=False)
        # Retournons enfin une réponse (status_code=200 par défaut) pour indiquer le succès de l'action
        return Response()

    @action(detail=True, methods=['post'], url_path='activer')
    def unable(self, request, pk):
        category = self.get_object()
        category.active = True
        category.save()
        category.products.update(active=True)
        return Response()
