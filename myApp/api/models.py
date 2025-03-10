from django.db import models


# Create your models here.
class Order(models.Model):
    number = models.IntegerField()
    customer_name = models.CharField(max_length=1000)
    date = models.DateField("Date", auto_now_add=True)


class Waypoint(models.Model):
    class TypeAddress(models.TextChoices):
        PICKUP = "PI", "Pickup"
        DELIVERY = "DE", "Delivery"

    order = models.ForeignKey("api.order", related_name="order", on_delete=models.CASCADE, blank=True)
    address = models.CharField(max_length=1000)
    type_address = models.CharField(max_length=2, choices=TypeAddress.choices, default=TypeAddress.DELIVERY)
