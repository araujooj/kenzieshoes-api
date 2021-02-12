from rest_framework.viewsets import ModelViewSet
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.models import Product
from rest_framework.filters import SearchFilter


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']
    permission_classes = [IsAuthenticatedOrReadOnly]
