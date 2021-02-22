from django.shortcuts import render

# Create your views here.


def wallet(request):
    """A view to return to sale page"""

    return render(request, 'wallet.html')
