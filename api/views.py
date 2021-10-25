from rest_framework import permissions
from rest_framework import viewsets
from .serializer import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticated]
