'''Checkout Admin'''

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    '''Admin class for OrderLineItem, allowing appending
    and editing of line items inside the Order model'''

    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    '''Admin class for Order models'''

    inlines = (OrderLineItemAdminInline,)

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

    ordering = ('-date',)
    # orders by date in reverse order, most recent first

admin.site.register(Order, OrderAdmin)
