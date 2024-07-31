from django.db import models

# Create your models here.
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name
