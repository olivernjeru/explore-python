'''
controls the admin page
'''
from django.contrib import admin
# import category and product from models.py within the store app
from .models import Category, Product

# make the classes for the database models created in models.py appear in the admin part of store app
# register Category model to the admin site of the store app
admin.site.register(Category)
# register Product model to the admin site of the store app
admin.site.register(Product)