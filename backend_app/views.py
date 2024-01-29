from django.shortcuts import render
from .models import Register, ExchangeRates
from .serializers import RegisterSerializer, ExchangeRatesSerializer
from rest_framework import viewsets

class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class ExchangeRatesView(viewsets.ModelViewSet):
    queryset = ExchangeRates.objects.all()
    serializer_class = ExchangeRatesSerializer