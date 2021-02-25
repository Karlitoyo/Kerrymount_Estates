from django.shortcuts import render

# Create your views here.


def wallet(request):
    """A view to return to sale page"""

    return render(request, 'wallet.html')


def add_to_wallet(request, item_id):
    """add property to wallet"""

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    date = request.POST.get('date')
    email = request.POST.get('email')
    duration = request.POST.get('duration')

    # redirect_url = request.POST.get('redrect_url')
    wallet = request.session.get('wallet', {})

    if item_id in list(wallet.keys()):
        wallet[item_id] = [first_name, last_name, date, email, duration]
    # wallet[item_id] = last_name
    # wallet[item_id] = email
    # wallet[item_id] = duration
    request.session['wallet'] = wallet
    print(request.session['wallet'])
    return render(request, 'wallet.html')
