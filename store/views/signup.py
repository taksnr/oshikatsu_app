from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (first_name, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "名前を入力してください!!"
        elif len (customer.first_name) < 3:
            error_message = '名前は3文字以上にしてください'
        elif len (customer.password) < 5:
            error_message = 'パスワードは5文字以上にしてください'
        elif len (customer.email) < 5:
            error_message = 'メールアドレスは5文字以上にしてください'
        elif customer.isExists ():
            error_message = 'このメールアドレスはすでに登録されています。。'
        # saving

        return error_message
