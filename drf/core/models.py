from django.db import models
from datetime import datetime as dt
from sandwiches.models import Sandwich

BREAD_TYPE_CHOICES = [
    (BROWN := 'brown', 'Brown'),
    (WHITE := 'white', 'White'),
]

class Order(models.Model):
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    email = models.EmailField()
    sandwich = models.ForeignKey(Sandwich, on_delete=models.SET_NULL, null=True, blank=False)
    bread_type = models.CharField(max_length=255, choices=BREAD_TYPE_CHOICES)
    
    # TODO: set auto_now_add to true and blank to false
    # the current settings allow the field to be edited via the admin panel
    order_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    # this is also only neccessary when wanting to edit order_date
    # via the admin panel
    def save(self, *args, **kwargs):
        if not self.id:
            self.order_date = dt.now()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.owner.username} ({str(self.order_date)})"

