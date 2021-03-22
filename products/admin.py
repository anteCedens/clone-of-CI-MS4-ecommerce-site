from django.contrib import admin
from .models import Product, Category, Publisher

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    Adjust the order here if we wish to
    change the order of the columns in the
    Django admin panel
    """
    list_display = (
        'sku',
        'name',
        'author',
        #'category',
        'price',
        'rating',
        'image',
    )

    """
    Place a minus in front of 'sku'
    to reverse the sorting order
    """
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'external_links',
        'image',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
