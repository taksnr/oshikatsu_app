from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware

#stripeのwebhook設定
from .views.checkout import my_webhook_view


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('stripe-webhook-paid/', my_webhook_view),

]
