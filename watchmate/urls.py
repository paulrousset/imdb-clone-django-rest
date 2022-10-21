from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("dashboard/", admin.site.urls),
    path("api/watchmate/", include("content_app.api.urls")),
    path("api/account/", include("user_app.api.urls")),
]
