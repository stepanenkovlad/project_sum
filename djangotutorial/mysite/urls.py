from django.contrib import admin
from django.urls import include, path
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('polls.urls_api')),  # Подключение API
    path('polls/', include('polls.urls')),    # Старые URL для "обычных" views
]