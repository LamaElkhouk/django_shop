from rest_framework.viewsets import ModelViewSet
from api.serializers import ProductSerializer, CreateProductSerializer
from api.models import Product


class ProductViewset(ModelViewSet):

    serializer_class = ProductSerializer
    create_serializer_class = CreateProductSerializer

    def get_serializer_class(self):
        # Si l'action demandée est retrieve nous retournons le serializer de détail
        if self.action == 'create':
            return self.create_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
