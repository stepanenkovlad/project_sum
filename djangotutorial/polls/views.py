from django.shortcuts import render
from django.http import HttpResponse
from .serializers import ProductSerializer, OrderSerializer
from .models import Product


# Стандартное Django-представление (можно оставить)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# DRF-представления для новых моделей
from rest_framework import viewsets
from .models import Product, Order  # Импортируем новые модели
from .serializers import ProductSerializer, OrderSerializer  # И новые сериализаторы

def product_list_html(request):
    products = Product.objects.all()
    return render(request, 'polls/product_list.html', {'products': products})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer