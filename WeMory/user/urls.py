from django.urls import path
from django.conf.urls import url 
from . import views


urlpatterns = [
    path('getCellCerti/', views.getCellCerti, name='getCellCerti'),
    path('signup/', views.signUp, name="signup"),
    path('signin/', views.signIn, name="signin"),
    path('getUserId/', views.getUserId, name='getUserId'),
 #   path('list/', views.user_list, name='user-list'),
    url(r'list/(?P<pk>[0-9]+)$', views.user_list, name="user-list"),
]
