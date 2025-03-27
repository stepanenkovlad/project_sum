from django.urls import path
from .views import product_list_html, index  # Добавили index

urlpatterns = [
    path('', index, name='index'),  # Для /polls/
    path('products/', product_list_html, name='product-list'),  # Для /polls/products/
]