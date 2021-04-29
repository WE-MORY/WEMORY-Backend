from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),
    path('verify/', verify_jwt_token),
    path('getCellCerti/', views.getCellCerti, name='getCellCerti'),
    path('executeCellCerti/', views.executeCellCerti, name='executeCellCerti'),
    path('signup/', views.createUser, name="signup"),
]
