'''Products views'''
from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    '''Returns all product pages, including Sorting and Searching'''

    products = Product.objects.all() # pylint: disable=E1101

    context = {
        'products' : products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    '''Returns details for single product'''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_detail.html', context)
