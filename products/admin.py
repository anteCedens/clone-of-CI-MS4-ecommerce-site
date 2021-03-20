from django.contrib import admin
from .models import Product, Category

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
        'category',
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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
