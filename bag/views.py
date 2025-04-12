'''Bag Views'''
from django.shortcuts import render, redirect

def view_bag(request):
    '''Returns bag page'''
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    '''Adds items to the bag'''

    # Fetch variables from page
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # If bag exists in session fetches it, else create empty bag
    bag = request.session.get('bag', {})

    # Adds item to bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # Pushes bag back to session
    request.session['bag'] = bag

    # Redirect to last page visited
    return redirect(redirect_url)
