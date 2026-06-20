from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class CustomOrder(admin.ModelAdmin):
    list_display = (
        "id",
        "total_price",
    )


@admin.register(OrderItem)
class CustomOrderItem(admin.ModelAdmin):
    list_display = (
        "order",
        "item",
    )
