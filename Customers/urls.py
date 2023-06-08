from django.urls import path

from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customers'),
    path('customer-add/', views.customer_add, name='customer_add'),
    path('customer-delete/<int:pk>', views.customer_delete, name='customer_delete'),
    path('customer-edit/<int:pk>', views.customer_edit, name='customer_edit'),
    path('customer-preview/<int:pk>', views.customer_preview, name='customer_preview'),
]