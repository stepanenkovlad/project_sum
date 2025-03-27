from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('polls.urls_api')),  # Подключение API
    path('polls/', include('polls.urls')),    # Старые URL для "обычных" views
]