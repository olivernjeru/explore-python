# Houses the DB for the userprofiles
from django.contrib.auth.models import User
from django.db import models

# User Profile Database Model
class Userprofile(models.Model):
    # defined a onetoonefield type of relationship and a cascade on delete
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    # a function that returns the username of a user
    def __str__(self) -> str:
        return self.user.username