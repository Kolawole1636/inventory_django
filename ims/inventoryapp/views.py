from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Category, Product, Stock, Customer, Supplier, IncomingOrder


def home(request):
    return render(request, "home.html")




def createcategory(request):

    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['desc']

        cat = Category(name=name, description=desc)
        cat.save()

        return redirect("allcat")

    else:
        return render(request, "createcategory.html")


def allcategory(request):

    all_cat = Category.objects.all()
    return render(request, "allcat.html", context={"all_cats":all_cat})



def removecat(request, id):

    cat = Category.objects.get(pk=id)
    cat.delete()
    return redirect("allcat")




def createproduct(request):

    cats = Category.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        available_quantity = 0
        unit_price = float(request.POST['price'])
        total_price = available_quantity * unit_price
        cat = request.POST['cat']

        cat = get_object_or_404(Category, name=cat)

        if Product.objects.filter(name=name).exists():
            return redirect("allproducts")

        else:
            product = Product(name=name, availableQuantity=available_quantity, unitPrice=unit_price,
                              totalPrice=total_price, categoryId=cat)
            product.save()

            return redirect("allproducts")

    else:
        return render(request, "createproduct.html", context={"allcats":cats})


def allproducts(request):

    products = Product.objects.all()

    return render(request, "allproducts.html", context={"allproducts": products})


def removeproduct(request, id):

    product = Product.objects.get(pk=id)

    product.delete()

    return redirect("allproducts")


def allstocks(request):

    stocks = Stock.objects.all()
    return render(request, "allstocks.html", context={"allstocks": stocks})


def createcustomer(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        email = request.POST['email']
        number = request.POST['number']
        address = request.POST['address']

        customer = Customer(firstName=fname, lastName=lname, age=age, email=email, phoneNumber=number, address=address)
        customer.save()

        return redirect("allcustomers")

    else:
        return render(request, "createcustomer.html")





def allcustomers(request):
    customers = Customer.objects.all()
    return render(request, "allcustomers.html", context={"customers":customers})


def removecustomer(request, id):

    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect("allcustomers")




def createsupplier(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        email = request.POST['email']
        number = request.POST['number']
        address = request.POST['address']

        customer = Customer(firstName=fname, lastName=lname, age=age, email=email, phoneNumber=number, address=address)
        customer.save()

        return redirect("allsuppliers")

    else:
        return render(request, "createsupplier.html")


def allsuppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "allsuppliers.html", context={"suppliers": suppliers})


def removesupplier(request, id):
    supplier = Supplier.objects.get(pk=id)
    supplier.delete()
    return redirect("allsuppliers")



def createincomingorder(request):

    products = Product.objects.all()
    suppliers = Supplier.objects.all()

    if request.method=="POST":
        supplier_name = request.POST['sname']
        product_name = request.POST['pname']
        quantity = request.POST['quantity']
        total_price = request.POST['price']

        supplier_name = get_object_or_404(Supplier, firstName=supplier_name)
        product_name = get_object_or_404(Product, name=product_name)

        order = IncomingOrder(productId=product_name, supplierId=supplier_name, quantityToSupply=quantity,
                              totalPrice=total_price)
        order.save()

        product = order.productId
        product.availableQuantity = IncomingOrder.objects.filter(productId=product).count()
        product.save()

        return redirect("allincomingorders")



    return render(request, "createincomingorder.html", context={"products":products, "suppliers": suppliers})






def allincomingorders(request):

    orders = IncomingOrder.object.all()
    return render(request, "allincomingorders.html", context={"orders": orders})


def removeincomingorder(request, id):
    order = IncomingOrder.objects.get(pk=id)
    order.delete()





