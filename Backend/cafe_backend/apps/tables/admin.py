from django.contrib import admin
from .models import Table


@admin.register(Table)
class CustomTable(admin.ModelAdmin):
    list_display = (
        "cafe",
        "table_ID",
        "price",
    )
