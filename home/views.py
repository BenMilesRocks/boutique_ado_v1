'''Renders page views'''
from django.shortcuts import render


def index(request):
    '''Returns index page'''
    return render(request, 'home/index.html')
