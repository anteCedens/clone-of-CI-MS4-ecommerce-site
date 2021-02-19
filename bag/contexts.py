from decimal import Decimal
"""
The decimal function is used here for financial
transactions - as using float is susceptible to rounding errors.
So just in general using decimal is preferred when working with money
because it's more accurate.
"""
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    This function will return a dictionary (instead of a template, for instance)
    called 'context'.
    This is what's known as a 'context processor'.
    It's purpose is to make this dictionary available to all templates
    across the entire app.
    In order for this to work, we need to add it to the list of
    context processors in settings.py
    """

    bag_items = []
    total = 0
    product_count = 0
    """
    This is the bag variable stored in the 'session':
    it contains all the items the user would like to purchase.
    """
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        # this is, the 'bag' from the 'session' above
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        """
        'free_delivery_delta' is there to let the users know
        how far from getting a free delivery are they
        """
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
