from django.shortcuts import render


def checkout(request):
    """A view to return to index page"""

    return render(request, 'checkout.html')
