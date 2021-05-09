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
]