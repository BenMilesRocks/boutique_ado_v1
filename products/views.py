'''Products views'''
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product

def all_products(request):
    '''Returns all product pages, including Sorting and Searching'''

    products = Product.objects.all() # pylint: disable=E1101

    #Sets search term to None, preventing issues if no search entered
    query = None

    if request.GET:
        # Check for search query, named 'q' in base.html
        if 'q' in request.GET:
            query = request.GET['q']
            # if search query blank
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            #Using Django 'Q' to filter search results
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            #Pass filter to Products
            products = products.filter(queries)

    context = {
        'products' : products,
        'search_term' : query,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    '''Returns details for single product'''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_detail.html', context)
