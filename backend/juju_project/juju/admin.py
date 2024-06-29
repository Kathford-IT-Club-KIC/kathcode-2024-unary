from django.contrib import admin
from .models import Business, MenuItem ,User,RestaurantOwner

admin.site.register(Business)
admin.site.register(MenuItem)
admin.site.register(User)
admin.site.register(RestaurantOwner)
