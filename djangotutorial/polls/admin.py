from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at")  # Поля в списке
    search_fields = ("name",)  # Поиск по названию

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "total_price", "created_at")
    filter_horizontal = ("products",)  # Удобный выбор товаров

admin.site.register(Product)
admin.site.register(Order)