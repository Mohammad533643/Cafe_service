from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Cafe(models.Model):
    name = models.CharField(max_length=250)
    cafe_ID = models.PositiveIntegerField(
        unique=True,
        validators=[
            MinValueValidator(100000),
            MaxValueValidator(999999),
        ]
    )
    Description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
    )
    Owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
