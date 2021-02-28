from django.contrib import admin
from .models import Product, Category

# below functions list the products within the admin section django


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'price',
        'name',
        'category',
        'description',
        'sku',
        'rating',
        'image'
    )

    ordering = ('price',)

# show friendly name of backend django admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
