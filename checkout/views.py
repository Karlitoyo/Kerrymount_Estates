from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from propertys.models import Product

from wallet.contexts import wallet_contents

import stripe

# checkout functon
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
# creates new instance of wallet or existing wallet
        wallet = request.session.get('wallet', {})
# takes date from form to allow checkout
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'full_address': request.POST['full_address'],
            'phone': request.POST['phone'],
            'email': request.POST['email'],
        }
# if form is valid takes information from above and saves data
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
# looks for specific information in wallet and progresses form to checkout confirmation if valid
            for item_id, item_data in wallet.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                        )
# nested if for above function not valid else block will search through quantity (redunant)
                    else:
                        for product in item_data['quantity'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the Propertys in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_wallet'))
# upon above successful order and requirments met below will progress form information for processing
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
# nested if order form not valid below else will show below message 
        else:
            messages.error(request, 'There was an error with your form. \
            Please double check your information.')
# else statement from initial if statement show wallet or create new wallet
    else:
        wallet = request.session.get('wallet', {})
        if not wallet:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('propertys'))
# stripe payment infirmation settings to progress payment
        current_wallet = wallet_contents(request)
        total = current_wallet['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total, currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
# error message will show if stripe public key is not available
    if not stripe_public_key:
        messages.warning(request, "Did you forget to set your public key in your enviornment?")
# returns checkout.html + context of order
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        }

    return render(request, template, context)

# checkout success function
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'wallet' in request.session:
        del request.session['wallet']

    template = 'checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
