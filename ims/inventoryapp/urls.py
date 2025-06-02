
from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name ='home'),

    path('createcat', views.createcategory, name='createcategory'),
    path('allcat', views.allcategory, name='allcat'),
    path('updatecat/<int:id>', views.updatecategory, name='updatecat'),
    path('removecat/<int:id>', views.removecat, name='removecat'),

    path('createproduct', views.createproduct, name='createproduct'),
    path('allproducts', views.allproducts, name='allproducts'),
    path('updateproduct/<int:id>', views.updateproduct, name='updateproduct'),
    path('removeproduct/<int:id>', views.removeproduct, name='removeproduct'),
    path("searchproduct", views.searchproduct, name="searchproduct"),

    path('createcustomer', views.createcustomer, name='createcustomer'),
    path('allcustomers', views.allcustomers, name='allcustomers'),
    path('updatecustomer/<int:id>', views.updatecustomer, name='updatecustomer'),
    path('removecustomer/<int:id>', views.removecustomer, name='removecustomer'),
    path("searchcustomer", views.searchcustomer, name="searchcustomer"),

    path('createsupplier', views.createsupplier, name='createsupplier'),
    path('allsuppliers', views.allsuppliers, name='allsuppliers'),
    path('updatesupplier/<int:id>', views.updatesupplier, name='updatesupplier'),
    path('removesupplier/<int:id>', views.removesupplier, name='removesupplier'),

    path('createincomingorder', views.createincomingorder, name='createincomingorder'),
    path('allincomingorders', views.allincomingorders, name='allincomingorders'),
    path('updateincomingorder/<int:id>', views.updateincomingorder, name='updateincomingorder'),
    path('removeincomingorder/<int:id>', views.removeincomingorder, name='removeincomingorder'),

    path('createoutgoingorder', views.createoutgoingorder, name='createoutgoingorder'),
    path('alloutgoingorders', views.alloutgoingorders, name='alloutgoingorders'),
    path('updateoutgoingorder/<int:id>', views.updateoutgoingorder, name='updateoutgoingorder'),
    path('removeoutgoingorder/<int:id>', views.removeoutgoingorder, name='removeoutgoingorder'),
    path("searchorder", views.searchorder, name="searchorder"),











]
