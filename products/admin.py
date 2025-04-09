'''Products Admin - register Product models here!'''
from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    '''Alters how Admin panel displays Product fields'''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image'
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    '''Alters how Admin panel displays Category fields'''
    list_display = (
        'friendly_name',
        'name'        
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
