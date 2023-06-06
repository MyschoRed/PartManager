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