from django.db import models
from apps.cafes.models import Cafe
from django.core.validators import MinValueValidator, MaxValueValidator


class Menu(models.Model):
    name = models.CharField(max_length=250)
    menu_ID = models.PositiveIntegerField(
        unique=True,
        validators=[
            MinValueValidator(100000),
            MaxValueValidator(999999)
        ])
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name="menu"
    )

    def __str__(self):
        return self.name


class Ithem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="ithem"
    )

    name = models.CharField(max_length=250)
    ithem_ID = models.PositiveIntegerField(
        unique=True,
        validators=[
            MinValueValidator(1)
        ])

    price = models.DecimalField(
        max_digits=30,
        decimal_places=3,
    )

    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True)

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
