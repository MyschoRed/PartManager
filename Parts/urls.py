from django.urls import path

from . import views

urlpatterns = [
    path('parts/', views.part_list, name='parts'),
    path('part-add/', views.part_add, name='part_add'),
    path('part-delete/<int:pk>', views.part_delete, name='part_delete'),
    path('part-edit/<int:pk>', views.part_edit, name='part_edit'),
]
