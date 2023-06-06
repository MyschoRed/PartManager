from django.db import models

from Customers.models import Customer
from Parts.models import Part


# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=4, unique=True, null=True, blank=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_customer')
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='order_part')
    pcs = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.order_id:
            last_object = Order.objects.order_by('-order_id').first()
            if last_object:
                last_value = int(last_object.order_id)
                self.order_id = str(last_value + 1).zfill(4)
            else:
                self.order_id = '0001'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_id} > {self.customer.name} > {self.part.part_id}"