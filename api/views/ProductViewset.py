from rest_framework.viewsets import ModelViewSet
from api.serializers import ProductSerializer
from api.models import Product


class ProductViewset(ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
