from rest_framework import generics, filters, permissions

from .models import Payments, User
from .serializers import PaymentSerializer, UserSerializer

# Create your views here.
class PaymentsListView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('date_payment',)
    ordering = ('-date_payment',)

    def get_queryset(self):
        queryset = Payments.objects.select_related('user', 'course', 'lesson')

        course_id = self.request.query_params.get('course')
        if course_id:
            queryset = queryset.filter(course_id=course_id)

        lesson_id = self.request.query_params.get('lesson')
        if lesson_id:
            queryset = queryset.filter(lesson_id=lesson_id)

        method_id = self.request.query_params.get('payment_method')
        if method_id:
            queryset = queryset.filter(payment_method=method_id)

        return queryset

class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()