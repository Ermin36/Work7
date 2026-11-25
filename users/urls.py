from django.urls import path
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import PaymentsListView, UserView, UserCreateAPIView
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('payments/', PaymentsListView.as_view(), name='payment-list'),
    path('user/me/', UserView.as_view(), name='user'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(permissions.AllowAny,)), name='login'),
    path('token/refresh/',
         TokenRefreshView.as_view(permission_classes=(permissions.AllowAny,)),
         name='token_refresh'),
]