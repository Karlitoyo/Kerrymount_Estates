from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):

    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('first_name', 'last_name', 'full_address',
                        'phone', 'email', 'order_total')

    fields = ('first_name', 'last_name', 'full_address',
                'phone', 'email', 'order_total')

    list_display = ('first_name', 'last_name', 'full_address',
                 'phone', 'email', 'order_total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)

