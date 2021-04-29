from django.urls import path
from . import views

urlpatterns = [
    path('getCellCerti/', views.getCellCerti, name='getCellCerti'),
    path('executeCellCerti/', views.executeCellCerti, name='executeCellCerti'),
    path('signup/', views.signUp, name="signup"),
    path('signin/', views.signIn, name="signin"),
]
