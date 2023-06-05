from django.contrib import admin

from core.models import Part, Customer, Order

# Register your models here.
admin.site.register(Part)
admin.site.register(Customer)
admin.site.register(Order)