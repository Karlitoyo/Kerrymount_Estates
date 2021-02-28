from django.shortcuts import render


def wallet(request):
    """A view to return to sale page"""

    return render(request, 'wallet.html')


def add_to_wallet(request, product_id):
    """add property to wallet"""

    quantity = int(request.POST.get('quantity'))

    wallet = request.session.get('wallet', {})

    if product_id in list(wallet.keys()):
        wallet[product_id] += quantity
    else:
        wallet[product_id] = quantity

    request.session['wallet'] = wallet
    return render(request, 'wallet.html')
