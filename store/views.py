from django.shortcuts import render, redirect
from django.http import JsonResponse, request, HttpResponse
import json
import datetime
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib import messages
from .forms import OrderForm, CreateUserForm
from django.views import generic
from .models import Customer, Product, User, OrderItem, ShippingAdress, Order
from .utils import cookieCart, cartData, guestOrder
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import Customer


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    print(items)
    print(items)

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)



def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order= data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def update_Item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)
    customername = request.user
    customer = Customer.objects.get(name=customername)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def dynamic_detail(request, x):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    prod = {"pronummer": x}
    products = Product.objects.all()

    context = {'products': products[x - 1], 'items': items, 'order': order, 'cartItems': cartItems}


    return render(request, "store/dynamic_detail.html", context)




def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customername = request.user
        customer = Customer.objects.get(name=customername)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        adress = data['address']
        #total = float(data['form']['total'])
        total = float(order.get_cart_total)
        cart = cartData(request)
        items = cart['items']  # list mit den prdoukten und preisen
        cartItems = cart['cartItems']
        items_quantityy = {}
        items_quantity = items


        for e, i in enumerate(items_quantity):
            Position = "Position" + str(e + 1)
            Menge = "Menge für Position" + str(e + 1)
            items_quantityy[Position] = items_quantity[e]["product"]["name"]
            items_quantityy[Menge] = items_quantity[e]["quantity"]


        order, created = Order.objects.get_or_create(customer=customer,
                                                         complete=True,
                                                         transaction_id=transaction_id,
                                                         adress=adress,
                                                         total=total,
                                                         items_quantity=items_quantityy
                                                         )
        order.save()

    else:
        name = data['form']['name']
        email = data['form']['email']
        adress = data['address']
        customer, created = Customer.objects.get_or_create(name=name, email=email)
        cart = cartData(request)
        items = cart['items']   #list mit den prdoukten und preisen
        cartItems = cart['cartItems']
        items_quantityy = {}
        items_quantity = items
        print(items)

        for e, i in enumerate(items_quantity):
            Position = "Position" + str(e +1)
            Menge = "Menge für Position" + str(e + 1)
            items_quantityy[Position] = items_quantity[e]["product"]["name"]
            items_quantityy[Menge] = items_quantity[e]["quantity"]

        print(items_quantityy)
        print("bis hier")

        total = float(data['form']['total'])
        transaction_id = transaction_id

        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=True,
                                                     transaction_id=transaction_id,
                                                     adress=adress,
                                                     total=total,
                                                     items_quantity=items_quantityy
                                                     )
        order.save()
        if order.shipping == True:
            ShippingAdress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )


        #for item in items:
            #product = Product.objects.get(id=item['product']['id'])
            #orderItem = OrderItem.objects.create(product=product, order=order, quantity=item['quantity'])
        # customer, order = guestOrder(request, data) obsolet, because alle above is in
    email_notification(request, customer, adress, transaction_id)
    return JsonResponse('Payment completeee!', safe=False)



def Impressum(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = { 'cartItems': cartItems}
    return render(request, "store/Impressum.html", context)


def Datenschutz(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = { 'cartItems': cartItems}
    return render(request, "store/Datenschutz.html", context)


def AGB(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = { 'cartItems': cartItems}
    return render(request, "store/AGB.html", context)


def Widerrufsbelehrung(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, "store/Widerrufsbelehrung.html", context)


def empty_your_cart(request):  # i think we can delete this

    cartItems = {}
    order = {}
    items = {}
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, "store/empty_your_cart.html", context)








def justregister(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = User.objects.create_user(username = username, email = email, password=password)# mey be call the variable just "user"
        #user_id = User.objects.raw('SELECT ID FROM auth_user WHERE username =' + username + '') #Abfrage aus der Tablle
        #for obj in user_id:
            #print(obj.id, obj.username)
            #x = obj.id
        customer = Customer.objects.get_or_create(name=username, email = email)

        #customer = authenticate(request, username=username, email=email)
        user = authenticate(request, username=username, password=password)
        #if user is not None:
            #login(request, user)
            #return redirect('login')
        context = {#'customer': customer, 'user': user
                   }

        return render(request, 'store/login.html', context)




def justlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # hier abfrage aus user tabelle mit email adressse aber nicht nötig
        customer = Customer.objects.get_or_create(name=username)
        context = {'user': user, 'customer': customer
                   }
        if user is not None:

            login(request, user) # importete method as an other name | bevor this change there was a login function wich conflict with the funktion
            #return redirect('store', context)
            return render(request, 'store/try_1.html', context)

    else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('login')
    return render(request, 'store/try_1.html', context)





def registerPage(request):
    #if request.user.is_authenticated:
        #messages.success(request, 'Sie sind bereits registriert, wenn sie ein neuen Account erstellen möchten bitte erst ausloggen')
        #return redirect('store')

    form = CreateUserForm()
        #if form.is_valid():
            #form.save()
            #user = form.cleaned_data.get('username')
            #return redirect('store')
    context = {'form': form}
    return render(request, 'store/registration.html', context)




def loginPage(request):
        return render(request, 'store/login.html')


def logoutUser(request):
    messages.success(request, 'Sie sind jetzt ausgeloggt')
    logout(request)
    return redirect('store')


def error_404(request, exception):
    context = {}
    return render(request, 'admin/page_not_found.html', context)



def error_500(request):
   context = {}
   return render(request,'admin/server_error_500.html', context)


def email_notification(request, customer, adress, transaction_id):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    customer = customer
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'name': customer, 'adress': adress, 'transaction_id': transaction_id}

    template = render_to_string('store/email_template.html', context)
    email = EmailMessage(
        'Danke für deinen Einkauf Bestellnummer: ' + str(transaction_id),
        template,
        settings.EMAIL_HOST_USER,
        [customer.email],  # change this to dynamic customer.email

    )
    email.fail_silently = False
    email.send()

    html_content = render_to_string('store/email_template2.html', context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        'Danke für deinen Einkauf Bestellnummer: ' + str(transaction_id),
        text_content,
        settings.EMAIL_HOST_USER,
        [customer.email],
    )
    email.attach_alternative(html_content, "text/html")
    email.send() # one of this is to delete


      
    template_vendor_email = render_to_string('store/vendor_notification.html', context)
    vendor_email = EmailMessage(
            'Neue Bestellung ' + str(transaction_id),
            template_vendor_email,
            settings.EMAIL_HOST_USER,
            ['tim.bretschneider95@gmail.com'],  #this have to be fix. its the vendor.
    )
    vendor_email.fail_silently = False
    vendor_email.send()


    #return render(request, 'store/store.html', context)