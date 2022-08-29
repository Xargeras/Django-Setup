from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    created = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    amount = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
