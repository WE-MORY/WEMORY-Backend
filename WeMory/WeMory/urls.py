from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-jwt-auth/', include('user.urls')),
]
