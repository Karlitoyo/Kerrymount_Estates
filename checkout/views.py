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
        'stripe_public_key': 'pk_test_5187i0yKX6mxq0Mg3EEWMwEpkMMCLJQFbaGKWR3s7jOTcHazAas1WC48VR2R7E52wVmMcNToexm2msbiiHMSxiRZ900w5fnxd6D',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
