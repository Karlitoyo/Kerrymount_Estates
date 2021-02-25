from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from wallet.contexts import wallet_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    wallet = request.session.get('wallet', {})
    if not wallet:
        messages.error(request, "There's nothing in your Wallet!'")
        return redirect(reverse('propertys'))

    current_wallet = wallet_contents(request)
    total = current_wallet['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total, currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_5187i0yKX6mxq0Mg3EEWMwEpkMMCLJQFbaGKWR3s7jOTcHazAas1WC48VR2R7E52wVmMcNToexm2msbiiHMSxiRZ900w5fnxd6D',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
