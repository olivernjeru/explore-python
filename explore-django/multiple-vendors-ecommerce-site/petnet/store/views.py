# import the render and get object if true and return 404 error instead of a server error
from django.shortcuts import render, get_object_or_404

# used .models because we are in the same folder
from .models import Product

# a function to render the product_detail.html file
# passed slug paremeter
def product_detail(request, slug):
    # set product to get the object Product, and pass the slug and if false, display the 404 error
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', #make it available in the template
    {
        'product': product
    })