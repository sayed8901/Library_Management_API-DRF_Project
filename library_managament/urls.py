from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('library/', include('library.urls')),
    path('activity/', include('activity.urls')),

    path("api-auth/", include("rest_framework.urls")),
]
