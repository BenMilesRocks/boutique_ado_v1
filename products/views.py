'''Products views'''
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

def all_products(request):
    '''Returns all product pages, including Sorting and Searching'''

    # Get all products from database
    products = Product.objects.all() # pylint: disable=E1101

    #Sets filter variables to None, preventing issues if not entered
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # Check for sort in response
        if 'sort' in request.GET:
            #fetch sort result
            sortkey = request.GET['sort']
            #push to variable
            sort = sortkey

            # use sortkey to check against products
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            # sort by category name, not category ID
            if sortkey == 'category':
                sortkey = 'category__name'

            # reverses list if direction == desc
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            # Apply sort to products
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products' : products,
        'search_term' : query,
        'current_categories' : categories,
        'current_sorting' : current_sorting
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    '''Returns details for single product'''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_detail.html', context)
