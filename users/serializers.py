from rest_framework import serializers

from .models import Payments, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('id', 'user', 'date_payment', 'lesson', 'course', 'amount', 'payment_method')


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payments', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'city', 'phone_number', 'payments')