'''Tools for the bag page'''
from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    '''calculate subtotal for bag items'''
    return price * quantity
