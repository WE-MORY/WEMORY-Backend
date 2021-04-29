from django.contrib import admin
from django.urls import path, include
import user, diary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('api/', include('diary.urls')),
]
