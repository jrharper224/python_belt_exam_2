from __future__ import unicode_literals
import datetime
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_user(self, post):
        isValid = True
        if len(post.get('name')) < 3:
            isValid = False
        if len(post.get('username')) < 3:
            isValid = False
        if len(post.get('password')) < 8:
            isValid = False
        if post.get('password') != post.get('password2'):
            isValid = False
        return isValid

    def login_user(self, post):
        user = self.filter(username = post.get('username')).first()
        name = self.filter(name = post.get('name'))
        if user.password == bcrypt.hashpw(post['password'].encode(), user.password.encode()):
            return (True, user, name)
        return (False, 'notuser')

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.EmailField(max_length=500)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class TripManager(models.Manager):

    def validate_trip(self, post):
        start = post.get('travel_start')
        end = post.get('travel_end')
        isValid = True
        if len(post.get('destination')) < 1:
            isValid = False
        if len(post.get('description')) < 1:
            isValid = False
        if len(post.get('travel_start')) < 1:
            isValid = False
        if len(post.get('travel_end')) < 1:
            isValid = False

        return isValid

class Trip(models.Model):
    destination = models.CharField(max_length = 500)
    description = models.CharField(max_length = 1200)
    travel_start = models.DateField()
    travel_end = models.DateField()
    going_on = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
