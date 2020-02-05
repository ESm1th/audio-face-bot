from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('bot.urls', namespace='bot')),
    path('admin/', admin.site.urls),
]
