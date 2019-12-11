from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Users(User, models.Model):
    username = User.username
    password = User.password
    email = User.email
    first_name = User.first_name
    last_name = User.last_name
    staf = User.is_staff
    last_login = User.last_login
    date_joined = User.date_joined
    age = models.DateField(auto_now=True)
    image_profile = models.ImageField(upload_to='uploads/image_profile', blank=True, default='default.jpeg')

    def __str__(self):
        return self.username
        