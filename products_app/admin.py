from django.contrib import admin
from .models import Category, Brand, Flavor, Ingredient, Product, ProductIngredient, Order, OrderItem

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Flavor)
admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(ProductIngredient)
admin.site.register(Order)
admin.site.register(OrderItem)