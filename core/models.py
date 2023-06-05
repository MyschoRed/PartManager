from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=128)
    boost_id = models.CharField(max_length=8)

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