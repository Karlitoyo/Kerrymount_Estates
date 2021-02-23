from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_propertys, name='propertys'),
    path('<product_id>', views.product_detail, name='property_detail'),
]
