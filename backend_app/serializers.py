from rest_framework import serializers
from .models import Register, ExchangeRates

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Register

class ExchangeRatesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ExchangeRates
