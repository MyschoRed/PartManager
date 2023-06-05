from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('customers/', views.customer_list, name='customers'),
    path('customer-add/', views.customer_add, name='customer_add'),
    path('customer-delete/<int:pk>', views.customer_delete, name='customer_delete'),
    path('customer-edit/<int:pk>', views.customer_edit, name='customer_edit'),

    path('parts/', views.part_list, name='parts'),
    path('part-add/', views.part_add, name='part_add'),
    path('part-delete/<int:pk>', views.part_delete, name='part_delete'),
    path('part-edit/<int:pk>', views.part_edit, name='part_edit'),
]