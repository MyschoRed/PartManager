from django.db import models

# Create your models here.

class Customer(models.Model):
    boost_id = models.CharField(max_length=5, unique=True, null=True, blank=True, editable=False)
    name = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.boost_id:
            last_object = Customer.objects.order_by('-boost_id').first()
            if last_object:
                last_value = int(last_object.boost_id)
                self.boost_id = str(last_value + 1).zfill(3)
            else:
                self.boost_id = '001'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.boost_id}"


class Part(models.Model):
    part_id = models.CharField(max_length=6, unique=True, null=True, blank=True, editable=False)
    description = models.CharField(max_length=512)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='part_customer')
    customer_part = models.CharField(max_length=128)
    revision = models.CharField(max_length=5, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.part_id:
            last_object = Part.objects.order_by('-part_id').first()
            if last_object:
                last_value = int(last_object.part_id)
                self.part_id = str(last_value + 1).zfill(6)
            else:
                self.part_id = '000001'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.part_id} - {self.customer_part}"

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
