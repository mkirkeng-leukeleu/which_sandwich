from django.db import models
from datetime import datetime as dt

# TODO: create models for sandwhiches
SANDWICH_CHOICES = [
    (OLDCHEESE := 'oldCheeseSandwich', 'Old cheese sandwich'),
    (OLDCHEESE := 'youngCheeseSandwich', 'Young cheese sandwich'),
    (OLDCHEESE := 'humusSandwich', 'Humus sandwich'),
]

BREAD_TYPE_CHOICES = [
    (BROWN := 'brown', 'Brown'),
    (WHITE := 'white', 'White'),
]

class Order(models.Model):
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    email = models.EmailField()
    sandwich = models.CharField(max_length=255, choices=SANDWICH_CHOICES)
    bread_type = models.CharField(max_length=255, choices=BREAD_TYPE_CHOICES)
    
    # TODO: set auto_now_add to true and blank to false
    # the current settings allow the field to be edited via the admin panel
    order_date = models.DateTimeField(auto_now_add=False, blank=True)

    def create(self, *args, **kwargs):
        self.order_date = dt.now()

        super().create(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.owner.username} ({str(self.order_date)})"
