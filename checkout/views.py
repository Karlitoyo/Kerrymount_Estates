from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    wallet = request.session.get('wallet', {})
    # if not wallet:
    #     messages.error(request, "There's nothing in your Wallet!'")
    #     return redirect(reverse('propertys'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
