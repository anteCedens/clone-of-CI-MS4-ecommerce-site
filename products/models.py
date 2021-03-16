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
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    """
    Each product will require a name, author, and price,
    but everything else is set as optional
    """
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.TextField(max_length=254)
    author = models.TextField(max_length=254)
    publisher = models.CharField(max_length=254, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    language = models.CharField(max_length=254, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class Author(models.Model):
    book_title = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    # name = models.ForeignKey(
        # 'Name', null=True, blank=True, on_delete=models.SET_NULL)
    name_and_surname = models.TextField(max_length=254)
    year_of_birth = models.IntegerField(null=True, blank=True)
    year_of_death = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    external_links = models.URLField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class Publisher(models.Model):
    book_title = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    publisher_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    external_links = models.URLField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)