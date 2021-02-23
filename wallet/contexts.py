from django.conf import settings


def wallet_contents(request):

    wallet_items = []
    total = 0
    property_count = 0

    context = {
        'wallet_items': wallet_items,
        'total': total,
        'property_count': property_count,
    }

    return context
