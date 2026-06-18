from django.db import models
from apps.cafes.models import Cafe
from django.core.validators import MinValueValidator, MaxValueValidator


class Table(models.Model):
    cafe = models.ForeignKey(Cafe,
                             on_delete=models.CASCADE,
                             related_name="tables")
    table_ID = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(1000)
    ])
    capacity = models.PositiveIntegerField(default=4)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=3,
    )

    class Neta:
        containers = [
            models.UniqueConstraint(
                fields=["cafe", "cafe_ID"],
                name="uniqe_table_ID_per_cafe"
            )
        ]

    def __str__(self):
        return f"{self.cafe} - table {self.table_ID}"
