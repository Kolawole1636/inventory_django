
from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('createcat', views.createcategory, name='createcategory'),
    path('allcat', views.allcategory, name='allcat'),
    path('removecat/<int:id>', views.removecat, name='removecat'),
    path('createproduct', views.createproduct, name='createproduct'),
    path('allproducts', views.allproducts, name='allproducts'),
    path('removeproduct/<int:id>', views.removeproduct, name='removeproduct'),
    path('createcustomer', views.createcustomer, name='createcustomer'),
    path('allcustomers', views.allcustomers, name='allcustomers'),
    path('removecustomer/<int:id>', views.removecustomer, name='removecustomer'),
    path('createsupplier', views.createsupplier, name='createsupplier'),
    path('allsuppliers', views.allsuppliers, name='allsuppliers'),
    path('removesupplier/<int:id>', views.removesupplier, name='removesupplier'),
    path('createincomingorder', views.createincomingorder, name='createincomingorder'),
    path('allincomingorders', views.allincomingorders, name='allincomingorders'),
    path('removeincomingorder/<int:id>', views.removeincomingorder, name='removeincomingorder'),
    path('createoutgoingorder', views.createoutgoingorder, name='createoutgoingorder'),
    path('alloutgoingorders', views.alloutgoingorders, name='alloutgoingorders'),
    path('removeoutgoingorder/<int:id>', views.removeoutgoingorder, name='removeoutgoingorder'),









]
