# models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RestaurantOwner(models.Model):
    restaurant_name = models.CharField(max_length=100)
    restaurant_address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.restaurant_name

class Business(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    business = models.ForeignKey(Business, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name
