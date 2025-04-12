'''Bag Views'''
from django.shortcuts import render

def view_bag(request):
    '''Returns bag page'''
    return render(request, 'bag/bag.html')
