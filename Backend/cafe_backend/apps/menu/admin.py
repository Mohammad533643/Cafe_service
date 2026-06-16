from django.contrib import admin
from .models import Menu, Ithem


@admin.register(Menu)
class CustomCafe(admin.ModelAdmin):
    list_display = (
        "name",
        "cafe",
    )


@admin.register(Ithem)
class CustomIthem(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )
