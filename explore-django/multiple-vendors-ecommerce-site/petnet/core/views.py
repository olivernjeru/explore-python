'''
This file is responsible for rendering pages once a user clicks and navigates
It renders the frontpage and the about page
'''

from store.models import Product, Category
from django.shortcuts import render

# function to render the frontpage.html file from the core app created and list the products added
def frontpage(request):
    # display products, slice only the first 6 to be displayed
    products = Product.objects.all()[0:6]
    return render(request, 'core/frontpage.html', {
        'products':products
    })

# function to render the about.html file from the core app created
def about(request):
    return render(request, 'core/about.html')
