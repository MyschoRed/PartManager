from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.order_list, name='orders'),
    path('order-add/', views.order_add, name='order_add'),
    path('order-delete/<int:pk>', views.order_delete, name='order_delete'),
    path('order-edit/<int:pk>', views.order_edit, name='order_edit'),
]