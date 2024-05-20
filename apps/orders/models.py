from django.db import models
from apps.common.models import TimeStampedUUIDModel

from apps.products.models import Product
from django.contrib.auth import get_user_model


User = get_user_model()


class OrderItem(TimeStampedUUIDModel):

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.buyer} - { self.item.name}"

    def get_total_price(self):

        if self.item.is_discounted:
            return self.item.discount_price * self.quantity

        return self.item.price * self.quantity


class Order(TimeStampedUUIDModel):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    orderItems = models.ManyToManyField(OrderItem)
    ordered_date = models.DateField(null=True, blank=True)

    ordered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.buyer.email

    def get_total_price(self):
        total = 0
        for item in self.orderItems.all():
            total += item.get_total_price()
        return total
