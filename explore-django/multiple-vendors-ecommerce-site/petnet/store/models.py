from tkinter import CASCADE
from unicodedata import category
from django.contrib.auth.models import User
from django.db import models

# Category Database Model
class Category(models.Model):
    title=models.CharField(max_length=50)
    # unique identifying part of a web address, typically at the end of the URL for example, Glossary/Slug
    slug = models.SlugField(max_length=50)

    # Fix display of words in the DB
    class Meta:
        # fix plural display of category from categorys to category
        verbose_name_plural = 'Categories'

    '''
    To fix the display of the created categories to display their respective names
    return the title of a category, I used the method below.
    It is called a method because it is within a class
    '''
    def __str__(self):
        return self.title

# Product model
class Product(models.Model):
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    # The on_delete=models.CASCADE means that if you delete a category, then you delete the products
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    title=models.CharField(max_length=50)
    # for the url display
    slug=models.SlugField(max_length=50)
    # description field that can be left null/blank
    description=models.TextField(blank=True)
    # price field that has the datatype integer
    price=models.IntegerField()
    # time field to track when the product was added
    created_at=models.DateTimeField(auto_now_add=True)
    # Show the time the product was updated
    updated_at=models.DateTimeField(auto_now=True)

    # Make new product added appear as the first one in sight of view
    class Meta:
        ordering = ('-created_at', )

    # To fix the display of the created categories to display their respective names
    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price /100