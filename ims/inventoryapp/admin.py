from django.contrib import admin

# Register your models here.

from .models import *

list1 = [Category, Product, Customer, Supplier, IncomingOrder, OutgoingOrder]


for item in list1:
    admin.site.register(item)
