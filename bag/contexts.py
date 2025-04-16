'''Bag contexts'''
from decimal import Decimal
from django.shortcuts import get_object_or_404
from boutique_ado.settings import FREE_DELIVERY_THRESHOLD, STANDARD_DELIVERY_PERCENTAGE
from products.models import Product

def bag_contents(request):
    '''Dict with shopping bag contents
    Available to any part of the application'''

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # Display bag contents
    for item_id, item_data in bag.items():

        # Check if item has size
        if isinstance(item_data, int):
            # If no size, just display bag contents
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product
            })
        else:
            # If has size, iterate through sizes and add them to bag one by one
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size' : size
                    })

    # Check if order qualifies for free delivery
    if total < FREE_DELIVERY_THRESHOLD:
        # Uses Decimal, as Float is prone to rounding errors
        delivery = total * Decimal(STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Total transaction
    grand_total = total + delivery

    context = {
        'total' : total,
        'product_count' : product_count,
        'delivery' : delivery,
        'grand_total' : grand_total,
        'free_delivery_delta' : free_delivery_delta,
        'bag_items' : bag_items,
        'free_delivery_threshold' : FREE_DELIVERY_THRESHOLD
    }

    return context
