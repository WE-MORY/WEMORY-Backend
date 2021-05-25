from django.urls import path
from django.conf.urls import url , include
from . import views

app_name = "diary"

urlpatterns = [
    path('diaries/', views.diary_list, name='diary-read'),
    url(r'diaries/(?P<pk>[0-9]+)$', views.diary_detail),
    path('goals/', views.goal_list, name='goal-read'),
#    url(r'diaries/(?P<pk>[0-9]+)$/(?P<date>\d{4}-\d{2}-\d{2})$', views.get_money),
#    url('^diaries/(?P<pk>.+)$/(?P<date>\d{4}-\d{2}-\d{2})$', MoneyList.as_view())
 ]
