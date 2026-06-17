from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from products_app.models import Product
from .cart import Basket
from .forms import *
from .models import Order, Pos_order


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', context={'basket': basket})


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['reload']
        )
    return redirect('basket_detail')


@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('product_list')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                buyer_firstname=form.cleaned_data['buyer_firstname'],
                buyer_name=form.cleaned_data['buyer_name'],
                buyer_surname=form.cleaned_data['buyer_surname'],
                comment=form.cleaned_data['comment'],
                delivery_address=form.cleaned_data['delivery_address'],
                delivery_type=form.cleaned_data['delivery_type']
            )
            for item in basket:
                Pos_order.objects.create(
                    product=item['product'],
                    count=item['count'],
                    order=order
                )
            basket.clear()
            return redirect('my_orders')
    return redirect('basket_detail')


@login_required
def open_order(request):
    context = {
        'form_order': OrderForm
    }
    return render(request, 'basket/order_form.html', context)


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-date_create')
    return render(request, 'basket/my_orders.html', {'orders': orders})