from django.db import models
from apps.cafes.models import Cafe
from apps.tables.models import Table
from apps.menu.models import Item


class Order(models.Model):
    cafe = models.ForeignKey(Cafe,
                             on_delete=models.CASCADE,
                             related_name="orders")
    table = models.ForeignKey(Table,
                              on_delete=models.CASCADE,
                              related_name="orders")

    created_at = models.DateTimeField(auto_now_add=True)

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0
    )

    def __str__(self):
        return f"order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name="order_items")
    item = models.ForeignKey(Item,
                             on_delete=models.PROTECT,
                             related_name="order_items")
    unit_price = models.DecimalField(
        max_digits=10,  # Because MenuItem.price is max 10 digit
        decimal_places=3,
    )

    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.order.total_price = sum(
            self.quantity * self.unit_price
            for item in self.order.order_items.all()
        )

        self.order.save(update_fields=["total_price"])
