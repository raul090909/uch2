from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('about/contacts/', contacts_view, name='contacts'),
    path('about/how-to-find/', how_to_find_view, name='how_to_find'),
    path('products/', products_view, name='products'),
    path('products/categories/', categories_view, name='categories'),
    path('products/all/', all_products_view, name='all_products'),
    path('cart/', cart_view, name='cart'),

    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('brand/list/', BrandListView.as_view(), name='brand_list'),
    path('brand/<int:pk>/', BrandDetailView.as_view(), name='brand_detail'),
    path('brand/create/', BrandCreateView.as_view(), name='brand_create'),
    path('brand/<int:pk>/update/', BrandUpdateView.as_view(), name='brand_update'),
    path('brand/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),

    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('order/list/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    path('flavor/list/', FlavorListView.as_view(), name='flavor_list'),
    path('flavor/<int:pk>/', FlavorDetailView.as_view(), name='flavor_detail'),
    path('flavor/create/', FlavorCreateView.as_view(), name='flavor_create'),
    path('flavor/<int:pk>/update/', FlavorUpdateView.as_view(), name='flavor_update'),
    path('flavor/<int:pk>/delete/', FlavorDeleteView.as_view(), name='flavor_delete'),
]