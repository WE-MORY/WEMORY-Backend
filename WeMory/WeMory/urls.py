from django.contrib import admin
from django.urls import path, include
import user, diary, account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('api1/', include('diary.urls')),
    path('api2/', include('account.urls')),
]
