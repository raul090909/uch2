from .views import *
from rest_framework import routers

urlpatterns = []

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('brand', BrandViewSet, basename='brand')
router.register('flavor', FlavorViewSet, basename='flavor')
router.register('ingredient', IngredientViewSet, basename='ingredient')
router.register('product', ProductViewSet, basename='product')
router.register('product-ingredient', ProductIngredientViewSet, basename='product-ingredient')
router.register('order', OrderViewSet, basename='order')
router.register('order-item', OrderItemViewSet, basename='order-item')

urlpatterns += router.urls