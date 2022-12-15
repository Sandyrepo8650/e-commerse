from django.contrib import admin
from .models import Product, Category, Order, OrderItem, ShippingAddress, Customer


admin.site.register([Product, Category, Customer, Order, OrderItem, ShippingAddress])