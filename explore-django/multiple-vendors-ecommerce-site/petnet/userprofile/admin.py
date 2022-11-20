'''
contains the admin page renders of databases created from the models.py classes
'''
from django.contrib import admin
# import userprofile class from models.py file within the same userprofile app
from .models import Userprofile

# adding userprofile to the frontend part of the admin in the website
admin.site.register(Userprofile)