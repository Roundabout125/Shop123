from django.urls import path
from django.views.generic import RedirectView
from . import views
from cbd_shop import settings

from django.views.static import serve
from django.conf.urls import handler404, handler500, handler403, handler400
handler404 = views.error_404
handler500 = views.error_500



urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.update_Item, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path('dynamic_detail/<int:x>/', views.dynamic_detail, name="dynamic_detail"),
    path('dynamic_detail/', views.dynamic_detail, name="dynamic_detail"),
    path('Impressum/', views.Impressum, name="Impressum"),
    path('Datenschutz/', views.Datenschutz, name="Datenschutz"),
    path('AGB/', views.AGB, name="AGB"),
    path('Widerrufsbelehrung/', views.Widerrufsbelehrung, name="Widerrufsbelehrung"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('justlogin/', views.justlogin, name="justlogin"),
	path('logout/', views.logoutUser, name="logout"),
	path('justregister/', views.justregister, name="justregister"),
	path('empty_your_cart/', views.empty_your_cart, name='empty_your_cart'),   #maybe this button later
   # path(r'^/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_URL2}),
    path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),

]

