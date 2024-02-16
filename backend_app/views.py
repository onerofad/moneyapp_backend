from django.shortcuts import render
from .models import Register, ExchangeRates, Transactions
from .serializers import RegisterSerializer, ExchangeRatesSerializer, TransactionSerializer
from rest_framework import viewsets

class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class ExchangeRatesView(viewsets.ModelViewSet):
    queryset = ExchangeRates.objects.all()
    serializer_class = ExchangeRatesSerializer

class TransactionView(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

