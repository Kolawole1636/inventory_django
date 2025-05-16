from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Category, Product, Customer, Supplier, IncomingOrder, OutgoingOrder


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

    total_price_for_all = 0

    for product in products:
        total_price_for_all += product.totalPrice

    return render(request, "allproducts.html", context={"allproducts": products, "total_price":total_price_for_all})


def removeproduct(request, id):

    product = Product.objects.get(pk=id)

    product.delete()

    return redirect("allproducts")



def searchproduct(request):

    cats = Category.objects.all()

    if request.method == "POST":
        cat_name = request.POST['catname']

        cat_name = get_object_or_404(Category, name=cat_name)

        products = Product.objects.filter(categoryId__exact=cat_name)

        return render(request, 'searchproduct.html', {"products": products, "cats": cats})

    return render(request, 'searchproduct.html', context={"cats": cats})



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



def searchcustomer(request):

    if request.method == "POST":
        customer_name = request.POST['cname']

        customers = Customer.objects.filter(firstName__icontains=customer_name)

        return render(request, 'searchcustomer.html', {"customers": customers})

    return render(request, 'searchcustomer.html')




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
        quantity = int(request.POST['quantity'])


        supplier_name = get_object_or_404(Supplier, firstName=supplier_name)
        product_name = get_object_or_404(Product, name=product_name)

        total_price = quantity * product_name.unitPrice

        order = IncomingOrder(productId=product_name, supplierId=supplier_name, quantityToSupply=quantity,
                              productPrice=product_name.unitPrice, totalPrice=total_price)
        order.save()

        product = order.productId
        product.availableQuantity = product.availableQuantity + quantity
        product.totalPrice = product.availableQuantity * product.unitPrice
        product.save()

        return redirect("allincomingorders")



    return render(request, "createincomingorder.html", context={"products":products, "suppliers": suppliers})


def allincomingorders(request):

    orders = IncomingOrder.objects.all()
    return render(request, "allincomingorders.html", context={"orders": orders})


def removeincomingorder(request, id):
    order = IncomingOrder.objects.get(pk=id)
    order.delete()
    return redirect("allincomingorders")


def createoutgoingorder(request):

    products = Product.objects.all()
    customers = Customer.objects.all()

    if request.method == "POST":

        customer_name = request.POST['cname']
        product_name = request.POST['pname']
        quantity = int(request.POST['quantity'])

        customer_name = get_object_or_404(Customer, firstName=customer_name)
        product_name = get_object_or_404(Product, name=product_name)

        total_price_before_discount = quantity * product_name.unitPrice

        discount = 0
        total_price_after_discount =0

        if product_name.availableQuantity >= quantity:

            if total_price_before_discount < 2000:
                discount = 0
                total_price_after_discount = total_price_before_discount

            elif 2000 < total_price_before_discount < 4000:
                discount = 10
                total_price_after_discount = total_price_before_discount - (total_price_before_discount*0.1)

            elif 4000 < total_price_before_discount < 8000:
                discount = 15
                total_price_after_discount = total_price_before_discount - (total_price_before_discount * 0.15)

            elif 8000 < total_price_before_discount < 12000:
                discount = 20
                total_price_after_discount = total_price_before_discount - (total_price_before_discount * 0.2)

            elif 12000 < total_price_before_discount < 15000:
                discount = 25
                total_price_after_discount = total_price_before_discount - (total_price_before_discount * 0.25)

            else:
                discount = 30
                total_price_after_discount = total_price_before_discount - (total_price_before_discount * 0.3)

            order = OutgoingOrder(productId=product_name, customerId=customer_name, quantityToOrder=quantity,
                                  totalPriceBeforeDiscount=total_price_before_discount, discount=discount,
                                  totalPriceAfterDiscount=total_price_after_discount)

            order.save()

            product = order.productId
            product.availableQuantity = product.availableQuantity - quantity
            product.totalPrice = product.availableQuantity * product.unitPrice
            product.save()

            return redirect("alloutgoingorders")

        else:
            messages.error(request, f'We do not have enough products in the stock!')
            return render(request, "stocks.html", context={"products": products})

    return render(request, "createoutgoingorder.html", context={"products":products, "customers": customers})



def alloutgoingorders(request):

    orders = OutgoingOrder.objects.all()
    return render(request, "alloutgoingorders.html", context={"orders": orders})


def removeoutgoingorder(request, id):
    order = OutgoingOrder.objects.get(pk=id)
    product = order.productId

    product.availableQuantity = product.availableQuantity + order.quantityToOrder
    product.totalPrice = product.availableQuantity * product.unitPrice

    product.save()
    order.delete()

    return redirect("alloutgoingorders")


def searchorder(request):

    if request.method == "POST":
        date1 = request.POST['date1']
        date2 = request.POST['date2']

        orders = OutgoingOrder.objects.filter(OrderDate__range=[date1, date2])

        total_price_for_all = 0

        for order in orders:
            total_price_for_all += order.totalPriceAfterDiscount

        return render(request, 'searchorder.html', {"orders": orders, "total_price":total_price_for_all})

    return render(request, 'searchorder.html')