from django.conf import settings
from django.shortcuts import get_object_or_404
from propertys.models import Product


def wallet_contents(request):

    wallet_items = []
    total = 0
    wallet = request.session.get('wallet', {})

    for item_id in wallet.items():
        product = get_object_or_404(Product, pk=item_id)
        total = product.price
        wallet_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'wallet_items': wallet_items,
        'total': total,
    }

    return context
