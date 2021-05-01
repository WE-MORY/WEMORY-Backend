from django.urls import path
from django.conf.urls import url 
from . import views

app_name = "post"

urlpatterns = [
    path('post', views.post_list, name='post-read'),
    url(r'post/(?P<pk>[0-9]+)$', views.post_detail),
]
