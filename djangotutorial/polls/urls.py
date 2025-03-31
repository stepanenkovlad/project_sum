from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet
from .views import product_list_html, index  # Добавили index

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('', index, name='index'),  # Для /polls/
    path('products/', product_list_html, name='product-list'),  # Для /polls/products/
]