from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet  # Импортируем новые ViewSet'ы

router = DefaultRouter()
router.register(r'products', ProductViewSet)  # Эндпоинт для продуктов
router.register(r'orders', OrderViewSet)     # Эндпоинт для заказов

urlpatterns = [
    path('', include(router.urls)),
]