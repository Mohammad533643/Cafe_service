from django.contrib import admin
from .models import Menu, Item


@admin.register(Menu)
class CustomCafe(admin.ModelAdmin):
    list_display = (
        "name",
        "cafe",
    )


@admin.register(Item)
class CustomIthem(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )
