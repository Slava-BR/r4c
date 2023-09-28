from django.db import models

from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False, default="1111-11-11 11:11:11")
    in_queue = models.BooleanField(blank=False, null=False, default=False)
