from django.conf import settings
from django.shortcuts import get_object_or_404
from propertys.models import Product


def wallet_contents(request):

    wallet_items = []
    total = 0
    product_count = 0
    wallet = request.session.get('bag', {})

    for item_id, quantity in wallet.items():
        product = get_object_or_404(Product, pk=item_id)
        total = product.price
        product_count += quantity
        wallet_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'wallet_items': wallet_items,
        'total': total,
        'product_count': product_count,
    }

    return context
