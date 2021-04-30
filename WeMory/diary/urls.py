from django.urls import path
from django.conf.urls import url 
from . import views

app_name = "diary"

urlpatterns = [
    path('diaries/', views.diary_list, name='diary-read'),
    url(r'diaries/(?P<pk>[0-9]+)$', views.diary_detail),
    path('diaries/post', views.post_list, name='post-read'),
    url(r'diaries/post/(?P<pk>[0-9]+)$', views.post_detail),
]
