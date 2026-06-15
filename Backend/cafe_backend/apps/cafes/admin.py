from django.contrib import admin
from .models import Cafe


@admin.register(Cafe)
class CustomCafe(admin.ModelAdmin):
    list_display = (
        "name",
        "cafe_ID"
    )
