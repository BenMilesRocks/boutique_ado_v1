'''Bag Views'''
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    '''Returns bag page'''
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    '''Adds items to the bag'''

    # Fetch variables from page
    product = Product.objects.get(pk=item_id) #pylint: disable=E1101
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Check for product size
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # If bag exists in session fetches it, else create empty bag
    bag = request.session.get('bag', {})

    # Check if product being added has a Size
    if size:

        # Check if this product already in the bag
        if item_id in list(bag.keys()):

            # If in bag, check if same size as one being added
            if size in bag[item_id]['items_by_size'].keys():
                # If True, increment quantity of item
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # Else add a new size and quantity
                bag[item_id]['items_by_size'][size] = quantity

        else:
            # If not in bag, add new dict to sort by size
            bag[item_id] = {'items_by_size': {size: quantity}}

    # If no size, add to bag
    else:

        # Check if already in bag
        if item_id in list(bag.keys()):
            # If in bag, increment quantity
            bag[item_id] += quantity
        else:
            # If not, add new key to bag
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    # Pushes bag back to session
    request.session['bag'] = bag

    # Redirect to last page visited
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    '''Amends the number of items in the bag'''

    # Fetch variables from page
    quantity = int(request.POST.get('quantity'))

    # Check for product size
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # If bag exists in session fetches it, else create empty bag
    bag = request.session.get('bag', {})

    # Check if product being altered has a Size
    if size:

        # If quantity > 0, update quantity
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        # If quantity == 0, delete item
        else:
            del bag[item_id]['items_by_size'][size]
            # If no other sizes in bag, delete item id completely
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

    # If no size, update quantity
    else:

        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
    # Pushes bag back to session
    request.session['bag'] = bag

    # Redirect to last page visited
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    '''Deletes item from bag'''

    try:
    # Check for product size
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        # If bag exists in session fetches it, else create empty bag
        bag = request.session.get('bag', {})

        # Check if product being altered has a Size
        if size:
            del bag[item_id]['items_by_size'][size]
            # If no other sizes in bag, delete item id completely
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)


        # Pushes bag back to session
        request.session['bag'] = bag

        # Redirect to last page visited
        return HttpResponse(status=200)

    except Exception as e: #pylint: disable=W0612,W0718
        return HttpResponse(status=500)
