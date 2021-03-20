from django.db import models

# Create your models here.


class Category(models.Model):

    """
    Use the 'Meta' class to change the Django
    inherent (mis)spelling of 'Categorys'
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.friendly_name
    # def __str__(self):
     #   return self.name

    # def get_friendly_name(self):
     #   return self.friendly_name


class Product(models.Model):
    category = models.ManyToManyField(
        Category, blank=True,
        help_text='Select a category for this book')
    """
    Each product will require a name, author, and price,
    but everything else is set as optional
    """
    sku = models.CharField('SKU', max_length=254, blank=True, unique=True)
    name = models.TextField(max_length=254)
    author = models.TextField(max_length=254)
    publisher = models.ForeignKey(
        'Publisher', null=True, on_delete=models.SET_NULL, related_name='+')
    # publisher = models.CharField(max_length=254, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    language = models.CharField(max_length=254, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField('Image URL', max_length=1024, blank=True)
    image = models.ImageField(blank=True)
    friendly_name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_publisher(self):
        return self.publisher


class Author(models.Model):
    author_name = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL, related_name='+')
    year_of_birth = models.PositiveIntegerField(
        null=True, blank=True)
    year_of_death = models.PositiveIntegerField(
        null=True, blank=True)
    bio = models.TextField(blank=True)
    external_links = models.URLField(blank=True)
    image_url = models.URLField('Image URL', max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.author_name


class Publisher(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    external_links = models.URLField(blank=True)
    image_url = models.URLField('Image URL', max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
