from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from users.models import User
from django.core.paginator import Paginator




def index(request):
    context = {
        'title': 'Store GO'
    }
    return render(request, 'products/index.html', context)


    def __str__(self):
        return self.name
    

def products(request, category_id=None, page=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page)

    

    content = {
        'title': 'Store - Catalog',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    }

    return render(request, 'products/products.html', content )


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete() 
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
