'''Checkout Admin'''

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    '''Admin class for Order models'''
    readonly_fields = (
        'order_number', 'date', 'delivery_cost',
        'order_total','grand_total'
        )

    fields = (
        'order_number', 'date', 'full_name',
        'email', 'phone_number', 'country',
        'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'county', 'delivery_cost',
        'order_total', 'grand_total'
    )

    list_display = (
        'order_number', 'date', 'full_name',
        'delivery_cost', 'order_total', 'grand_total'
    )

    ordering = '-date'
    # orders by date in reverse order, most recent first
