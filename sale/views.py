from django.shortcuts import render

# Create your views here.


def sale(request):
    """A view to return to sale page"""

    return render(request, 'sale.html')
