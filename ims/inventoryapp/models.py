from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie"


class Product(models.Model):
    name = models.CharField(max_length=30, null=False)
    categoryId = models.ForeignKey(Category, related_name="product", on_delete=models.CASCADE)
    availableQuantity = models.IntegerField(default=0)
    unitPrice = models.FloatField(default=0)
    totalPrice = models.FloatField(default=0)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    age = models.IntegerField()
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length=45)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.firstName


class Supplier(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    age = models.IntegerField()
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length=45)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.firstName


class IncomingOrder(models.Model):
    productId = models.ForeignKey(Product, default=0, related_name="incomingorder", on_delete=models.CASCADE)
    supplierId = models.ForeignKey(Supplier, default=0,related_name="incomingorder", on_delete=models.CASCADE)
    quantityToSupply = models.IntegerField()
    productPrice = models.FloatField()
    totalPrice = models.FloatField()
    supplyDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.supplierId.firstName


class OutgoingOrder(models.Model):
    productId = models.ForeignKey(Product, default=0, related_name="outgoingorder", on_delete=models.CASCADE)
    customerId = models.ForeignKey(Customer, default=0, related_name="outgoingorder", on_delete=models.CASCADE)
    quantityToOrder = models.IntegerField()
    totalPriceBeforeDiscount = models.FloatField()
    discount = models.FloatField()
    totalPriceAfterDiscount = models.FloatField()
    OrderDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customerId.firstName




