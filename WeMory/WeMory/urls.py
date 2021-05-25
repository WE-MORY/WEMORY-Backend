from django.contrib import admin
from django.urls import path, include
import user, diary, account, post
from django.db import router
from rest_framework import routers
from diary.views import PostViewSet

router = routers.DefaultRouter()
router.register('money', PostViewSet, basename='money')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('users/', include('user.urls')),
    path('api1/', include('diary.urls')),
    path('api2/', include('account.urls')),
    path('api3/', include('post.urls')),
]
