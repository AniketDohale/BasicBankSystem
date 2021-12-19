from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import Customers, Transfer
from django.contrib import messages
from django.db import transaction
from .forms import CustomerFrom

# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def customers(request):
    custom = Customers.objects.all
    return render(request, 'customers.html', {'custom': custom})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def payment(request, cust_id):
    custom = Customers.objects.get(cust_id=cust_id)
    if request.method == 'POST':
        try:
            sender = request.POST.get('from_user')
            to_user = request.POST.get('to_user')
            cus_amount = request.POST.get('amount')
            amt = int(cus_amount)

            if to_user == '':
                messages.warning(request, "Please provide Receiver's name")

            elif amt <= 0:
                messages.warning(
                    request, 'Please provide valid money details!!')

            else:
                with transaction.atomic():
                    from_user_obj = Customers.objects.get(first_name=sender)
                    from_user_obj.cust_amount -= int(cus_amount)
                    from_user_obj.save()

                    to_user_obj = Customers.objects.get(
                        first_name=to_user)
                    to_user_obj.cust_amount += int(cus_amount)
                    to_user_obj.save()

                    data = Transfer(from_cust=sender,
                                    to_cust=to_user, cust_amount=cus_amount)
                    data.save()

                    messages.warning(request, 'Your amount is transferred')
                    return redirect('trans_history')

        except Exception as e:
            print(e)
            messages.success(request, 'Something Went Wrong')

    return render(request, 'payment.html', {'custom': custom})


def trans_history(request):
    trans = Transfer.objects.all
    return render(request, 'trans_history.html', {'trans': trans})
