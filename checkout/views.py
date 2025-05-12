'''Checkout Views'''
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    '''Checkout view. Pulls bag from session, else displays error'''
    bag = request.session.get('bag', {})
    if not bag:
        # If bag empty display error
        messages.error(request, "There's nothing in your bag!")
        # Redirect back to products, preventing users from entering URL
        # to access the Checkout Page without adding products to bag
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,

    }

    return render(request, template, context)
