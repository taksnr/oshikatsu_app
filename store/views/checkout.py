

#stripe設定
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys

import stripe
stripe.api_key = 'sk_test_51M5omJHrs4Z3uUHoUmiNWnEr2HB3pEkHmHEjudfseidlY25wz6yTZZofJ2CsENw5ynKLljoOano6hT5LY9s0dWIu004CpA7hva'
DJSTRIPE_WEBHOOK_SECRET = "whsec_8b126b8c40c1b3419cccadae2a3ca7f1ddd55cc7272a60533330d6edb976395c"
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #CSRFTOKEN　を無効化
from django.shortcuts import render , redirect #webhook受取⇨redirect order,かつ　orderに情報セーブ

from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
@require_POST
# Using Django
@csrf_exempt
def my_webhook_view(request):
  payload = request.body
  event = None

  try:
    event = stripe.Event.construct_from(
      json.loads(payload), stripe.api_key
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  

   # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
        checkout_session = event['data']['object']
        # Make sure is already paid and not delayed
        if checkout_session.payment_status == "paid":
            _handle_successful_payment(checkout_session)

    # Passed signature verification

  return HttpResponse(status=200)

from store.models.product import Products
from store.models.orders import Order
from store.models.customer import Customer
from django.shortcuts import render, redirect
from django.views import  View


from django.contrib.auth.hashers import check_password


def _handle_successful_payment(checkout_session, self, request):
  cart = request.session.get('cart')
  products = Products.get_products_by_id(list(cart.keys()))
  customer = request.session.get('customer')
       

  for product in products:
        print(cart.get(str(product.id)))
        order = Order(customer=Customer(id=customer),
                      product=product,
                      price=product.price,)
        order.save()
  request.session['cart'] = {}
#購入後履歴に飛ばす
#addressを追加して欲しい機能、phoneをその他要望に変更
  return redirect('orders')
    # Define what to do after the user has successfully paid
    
#orderに購入履歴をPOST,ordersにリダイレクト








#とりあえずお支払いボタン押した瞬間起動
#webhook受取後、orderにデータsave()


class CheckOut(View):
    def post(self, request):
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        customer = request.session.get('customer')
       

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,)
            order.save()
        request.session['cart'] = {}
#購入後履歴に飛ばす
#addressを追加して欲しい機能、phoneをその他要望に変更
        return redirect('orders')