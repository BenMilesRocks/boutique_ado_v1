'''Products views'''
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

def all_products(request):
    '''Returns all product pages, including Sorting and Searching'''

    # Get all products from database
    products = Product.objects.all() # pylint: disable=E1101

    #Sets filter variables to None, preventing issues if not entered
    query = None
    categories = None

    if request.GET:
        # Check for category in response
        if 'category' in request.GET:
            #Split into list, divided by commas
            categories = request.GET['category'].split(',')
            #Filter products by items in list
            products = products.filter(category__name__in=categories)
            #Filter Category by selected categories
            categories = Category.objects.filter(name__in=categories) # pylint: disable=E1101

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
        'current_categories' : categories,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    '''Returns details for single product'''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_detail.html', context)
