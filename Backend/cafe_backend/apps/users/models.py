from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone = models.CharField(
        max_length=10,
        unique=True
    )

    email = models.EmailField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )

    class UserRole(models.TextChoices):
        CUSTOMER = "customer", "Customer"
        MANAGER = "manager", "Manager"
        OWNER = "owner", "Owner"
        STAFF = "staff", "Staff"

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CUSTOMER
    )

    def __str__(self):
        return self.username
