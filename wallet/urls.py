from django.urls import path
from .import views

urlpatterns = [
    path('', views.wallet, name='wallet'),
    path('add/<product_id>', views.add_to_wallet, name='add_to_wallet'),
]
