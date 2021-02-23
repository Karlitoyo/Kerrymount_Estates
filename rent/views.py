from django.shortcuts import render

# Create your views here.


def rent(request):
    """A view to return to index page"""

    return render(request, 'rent.html')

