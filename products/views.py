'''Products views'''
from django.shortcuts import render
from .models import Product

def all_products(request):
    '''Returns all product pages, including Sorting and Searching'''

    products = Product.objects.all() # pylint: disable=E1101

    context = {
        'products' : products,
    }

    return render(request, 'products/products.html', context)
