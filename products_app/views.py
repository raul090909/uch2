from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Brand, Category, Order, Flavor



def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def how_to_find_view(request):
    return render(request, 'how_to_find.html')

def products_view(request):
    return render(request, 'products.html')

def categories_view(request):
    return render(request, 'categories.html')

def all_products_view(request):
    return render(request, 'all_products.html')

def cart_view(request):
    return render(request, 'cart.html')



class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_form.html'
    fields = ['name', 'description', 'price', 'weight', 'photo', 'is_available', 'category', 'brand', 'flavors']
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_form.html'
    fields = ['name', 'description', 'price', 'weight', 'photo', 'is_available', 'category', 'brand', 'flavors']
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')



class BrandListView(ListView):
    model = Brand
    template_name = 'brand/brand_list.html'
    context_object_name = 'brands'

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand/brand_detail.html'
    context_object_name = 'brand'

class BrandCreateView(CreateView):
    model = Brand
    template_name = 'brand/brand_form.html'
    fields = ['name', 'country', 'description', 'logo']
    success_url = reverse_lazy('brand_list')

class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'brand/brand_form.html'
    fields = ['name', 'country', 'description', 'logo']
    success_url = reverse_lazy('brand_list')

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brand/brand_confirm_delete.html'
    success_url = reverse_lazy('brand_list')



class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category/category_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category/category_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')



class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order/order_form.html'
    fields = ['customer_name', 'customer_email', 'customer_phone', 'status']
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order/order_form.html'
    fields = ['customer_name', 'customer_email', 'customer_phone', 'status']
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')



class FlavorListView(ListView):
    model = Flavor
    template_name = 'flavor/flavor_list.html'
    context_object_name = 'flavors'

class FlavorDetailView(DetailView):
    model = Flavor
    template_name = 'flavor/flavor_detail.html'
    context_object_name = 'flavor'

class FlavorCreateView(CreateView):
    model = Flavor
    template_name = 'flavor/flavor_form.html'
    fields = ['name']
    success_url = reverse_lazy('flavor_list')

class FlavorUpdateView(UpdateView):
    model = Flavor
    template_name = 'flavor/flavor_form.html'
    fields = ['name']
    success_url = reverse_lazy('flavor_list')

class FlavorDeleteView(DeleteView):
    model = Flavor
    template_name = 'flavor/flavor_confirm_delete.html'
    success_url = reverse_lazy('flavor_list')