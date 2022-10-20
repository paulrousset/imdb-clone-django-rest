from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('api/watchmate/', include('content_app.api.urls')),
]
