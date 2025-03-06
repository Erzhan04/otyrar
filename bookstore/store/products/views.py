from django.shortcuts import render
from products.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'Store GO'
    }
    return render(request, 'products/index.html', context)


    def __str__(self):
        return self.name
def products(request):
    content = {
        'title': 'Store - Catalog',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/products.html', content )