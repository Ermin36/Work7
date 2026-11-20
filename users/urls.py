from django.urls import path
from .views import PaymentsListView, UserView

urlpatterns = [
    path('payments/', PaymentsListView.as_view(), name='payment-list'),
    path('user/me/', UserView.as_view(), name='user'),
]