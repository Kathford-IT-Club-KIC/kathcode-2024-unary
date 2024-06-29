# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userlogin/', views.user_login_view, name='userlogin'),
    path('ownerlogin/', views.owner_login_view, name='ownerlogin'),
    path('userdashboard/', views.user_dashboard, name='user_dashboard'),
    path('ownerdashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('map/', views.map, name='map'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart_view, name='cart'),
    path('ownerorderdetails/', views.ownerorderdetails, name='ownerorderdetails'),
    path('ownerhome/', views.ownerhome, name='ownerhome'),
    path('usermenu/', views.usermenu, name='usermenu'),

]