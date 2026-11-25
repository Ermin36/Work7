from rest_framework import serializers

from .models import Payments, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('id', 'user', 'date_payment', 'lesson', 'course', 'amount', 'payment_method')


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'city', 'phone_number', 'payments', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user