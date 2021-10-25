from django import urls
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('product', views.ProductViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    # Urls de registro y autenticación
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration', include('rest_auth.registration.urls')),
]
