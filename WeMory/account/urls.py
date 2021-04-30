from django.urls import path
from django.conf.urls import url 
from . import views

app_name = "account"

urlpatterns = [
    path('accounts/', views.account_list, name="account-list"),
    url(r'accounts/(?P<pk>[0-9]+)$', views.account_detail),
]