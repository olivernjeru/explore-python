# Controls the movement from one page to another via importing pages and also through url patterns
from django.contrib import admin
from django.urls import path

# Import frontpage and about from the views.py file in core app
from core.views import frontpage, about

# Import from store app, in the views.py file, product_detail file
from store.views import product_detail

urlpatterns = [
    # define path for product detail view. we have imported this from the view.py file in the store app
    # so when the urlpatterns list runs, we will start with the path for the product detail in the url then continue to the rest
    path('<slug:slug>', product_detail, name='product_detail'),
    # define path for the frontpage, no path included because its the default page
    path('', frontpage, name='frontpage'),
    # define path for the about
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]
