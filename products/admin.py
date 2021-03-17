from django.contrib import admin
from .models import Product, Category, Author, Publisher

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
        'friendly_name',
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


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'year_of_birth',
        'year_of_death',
        'bio',
        'external_links',
        'image',
    )


class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'external_links',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
