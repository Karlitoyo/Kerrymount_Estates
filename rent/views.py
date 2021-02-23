from django.shortcuts import render


def rent(request):
    """A view to return to index page"""

    return render(request, 'rent.html')

