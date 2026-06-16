from rest_framework import serializers
from products_app.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 
                  'description']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 
                  'description', 
                  'country', 
                  'logo']

class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ['name']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 
                'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 
                  'description', 
                  'price', 
                  'weight', 
                  'photo', 
                  'is_available', 
                  'category', 
                  'brand', 
                  'flavors']

class ProductIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIngredient
        fields = ['product', 
                  'ingredient', 
                  'amount_mg']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer_name', 
                  'customer_email', 
                  'customer_phone', 
                  'status', 
                  'created_at']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 
                  'product', 
                  'quantity', 
                  'price'
                  ]
#price = serializers.DecimalField(label='Цена', max_degits=10, decimal_places=2)это для цены