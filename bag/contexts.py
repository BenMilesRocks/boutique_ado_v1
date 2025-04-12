'''Bag contexts'''
from decimal import Decimal
from boutique_ado.settings import FREE_DELIVERY_THRESHOLD, STANDARD_DELIVERY_PERCENTAGE

def bag_contents(request):
    '''Dict with shopping bag contents
    Available to any part of the application'''

    bag_items = []
    total = 0
    product_count = 0

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
