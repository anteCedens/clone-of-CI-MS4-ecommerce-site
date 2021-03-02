from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# 'Q' is used to generate a search query (mainly the 'OR' logic bit)
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower

# Create your views here.


def all_products(request):
    # A view to show all products, including sorting and search queries

    """
    Randomize the display of products on each load (i.e. reshuffle).
    Note warning/caveat on:
    https://docs.djangoproject.com/en/3.1/ref/models/querysets/#order-by:
        "Note: order_by('?') queries may be expensive and slow,
        depending on the database backend you’re using."
    Should this prove too cumbersome, just replace with:
        "products = Product.objects.all()".
    Products will then be ordered by 'SKU'.
    """
    products = Product.objects.order_by('?')
    # Set these intially to 'None', so as not cause errors
    query = None
    sort = None
    direction = None
    categories = None

    if request.GET:
        if 'sort' in request.GET:
            """
            The reason for copying the sort parameter into a new variable
            called sortkey is to preserve the original field we want it to
            sort on (i.e. 'name').
            If we had just renamed 'sort' itself to 'lower_name', we would
            have lost the original field 'name'.
            """
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                # Annotation allows us to add a temporary field on a model
                # Our goal with 'Lower' is to make the sorting case-insensitive
                products = products.annotate(lower_name=Lower('name'))
            # This makes so categories are sorted by their name instead of id
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    # Adding a minus reverses the sorting order
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        """
        'q' is the value of the 'name' attribute
        assigned to the search bar in base.html
        """
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria...")
                return redirect(reverse('products'))

            """
            The pipe ('|') is what generates the OR statement/logic
            for the queries,
            and the 'i' in front of 'contains' makes
            the queries case insensitive
            """
            queries = Q(name__icontains=query) | Q(author__icontains=query)
            products = products.filter(queries)

    # If no sorting is selected, 'current_sorting' value will be 'None_None'
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    # A view to show individual product details

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
