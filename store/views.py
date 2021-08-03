from django.shortcuts import render, redirect
from .models import *  # hier werden die Classen aus der models.py importiert
from django.http import JsonResponse, request, HttpResponse
from django.views.generic.detail import DetailView
from django.forms import inlineformset_factory
import json
import datetime
from .models import *

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from .forms import OrderForm, CreateUserForm
from django.contrib import messages
from .forms import OrderForm, CreateUserForm

#from django.contrib.auth.decorators import login_required


# Create your views here.


def registration(request):
    if request.user.is_authenticated:
        return redirect('store')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
             form = CreateUserForm(request.POST)
             if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                #messages.success(request, 'Der Account wurde für ' + user+ 'angelegt')

                return redirect('store')

        context = {'form':form}
        return render(request, "store/registration.html", context)


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

    # i think here comes the part of deleting everthing from the cart


#def dynamic_detail(request):
    # data = json.loads(request.body)
    # productId = data['productname']
    # action = data['action']
    # if action == 'view':
    # pass
    # filtername = request.Product.id
    # products = Product.objects.filter(name=filtername)
    # products = Product.objects.filter
    # context = {'products': products}
    # product = Product.objects.get(id=productId)
    # context = {'products': product}
    # context = "CBD Kolb-Kush"
    #return render(request, 'store/dynamic_detail.html'  # , context
                #  )  # ,  we have to give some values out of the models and i dont know how


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def update_Item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
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
    #data = json.loads(request.body)
    #productId = data['productId']
   # products = {"productId": productId}
   # print(products)
    #products = Product.objects.all()
  #  context = {'products': products}
    prod = {"pronummer": x }
    products = Product.objects.all()
    #for e in products:
     #   long_description = str(e.long_description)
      #  long_descriptions =+ str(long_description.replace(' ', '<br>'))
    context = {'products': products[x-1]#, 'long_description': long_descriptions
               }


    #note = note.replace('\n', '<br>')



    return render(request, "store/dynamic_detail.html", context
                  #+ productId + "/.html"
    # ,context
    )



def tryi(request, x):
    y = x
    data = json.loads(request.body)
    productId = data['productId']
    print(productId)
    return render(request, "try_1.html", )


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
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

    else:
        print("user not logged in ")
    return JsonResponse('Payment complete!', safe=False)






def Impressum(request):
    return render(request, "store/Impressum.html")


def Datenschutz(request):
    return render(request, "store/Datenschutz.html")


def AGB(request):
    return render(request, "store/AGB.html")

def Widerrufsbelehrung(request):
    return render(request, "store/Widerrufsbelehrung.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('store')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('store')
            else:
                messages.info(request, 'Name oder Passwort stimmt nicht Kollege')

        context = {}
        return render(request,"store/login.html", context)



def logout(request):
    logout(request)
    return redirect('login')



