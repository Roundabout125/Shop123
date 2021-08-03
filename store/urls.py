from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.update_Item, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
	path('dynamic_detail/<int:x>/', views.dynamic_detail, name="dynamic_detail"),
    path('dynamic_detail/', views.dynamic_detail, name="dynamic_detail"),
    path('Impressum/', views.Impressum, name="Impressum"),
    path('Datenschutz/', views.Datenschutz, name="Datenschutz"),
    path('AGB/', views.AGB, name="AGB"),
    path('Widerrufsbelehrung/', views.Widerrufsbelehrung, name="Widerrufsbelehrung"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('logout/', views.logout, name="logout"),
    #path('try/<int:x>/', views.tryi , name="try"),
]