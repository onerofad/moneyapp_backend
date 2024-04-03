from rest_framework import serializers
from .models import Register, ExchangeRates, Transactions, PaymentMethod

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Register

class ExchangeRatesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ExchangeRates

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Transactions

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PaymentMethod

