from django.db import models

class Product(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} ({self.price} руб.)"

class Order(models.Model):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    client_name = models.CharField(max_length=100,
        default="Unknown",  # Добавь осмысленный default
        verbose_name="Client Name")

    def __str__(self):
        return f"Заказ #{self.id} от {self.client_name}"