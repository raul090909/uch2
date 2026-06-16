from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, filters
from products_app.models import *
from .permission import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']

class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class ProductIngredientViewSet(viewsets.ModelViewSet):
    queryset = ProductIngredient.objects.all()
    serializer_class = ProductIngredientSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer_name', 'customer_email', 'status']

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage