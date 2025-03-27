from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Order(models.Model):
    products = models.ManyToManyField(Product, verbose_name="Товары")
    total_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0,
        verbose_name="Общая сумма"
    )
    customer_name = models.CharField(max_length=100, verbose_name="Имя заказчика")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")

    def __str__(self):
        return f"Заказ #{self.id} от {self.customer_name}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"