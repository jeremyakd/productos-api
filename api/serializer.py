from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = ['name', 'price', 'description'] # para especificar campo
        # fields = '__all__'
        exclude = ['created', 'updated'] # para excluir campo