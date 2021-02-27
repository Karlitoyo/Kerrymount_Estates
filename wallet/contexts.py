from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from propertys.models import Product


def wallet_contents(request):

    wallet_items = []
    total = 0
    product_count = 0
    quantity = 0
    wallet = request.session.get('wallet', {})

    for product_id, product in wallet.items():
        product = get_object_or_404(Product, pk=product_id)
        total = product.price
        # product_count += quantity
        wallet_items.append({
            'product_id': product_id,
            'product': product,
            'quantity': quantity,
        })

    context = {
        'wallet_items': wallet_items,
        'total': total,
        'product_count': product_count,
    }

    return context
