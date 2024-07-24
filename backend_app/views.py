from .models import Register, ExchangeRates, Transactions, PaymentMethod, BankInfo, Recepients, TemporaryTransactions
from .serializers import RegisterSerializer, ExchangeRatesSerializer, TransactionSerializer, PaymentMethodSerializer, BankInfoSerializer, RecepientSerializer, TemporaryTransactionSerializer
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

class RecepientView(viewsets.ModelViewSet):
    queryset = Recepients.objects.all()
    serializer_class = RecepientSerializer


class PaymentMethodView(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class BankInfoView(viewsets.ModelViewSet):
    queryset = BankInfo.objects.all()
    serializer_class = BankInfoSerializer

class TemporaryTransactionView(viewsets.ModelViewSet):
    queryset = TemporaryTransactions.objects.all()
    serializer_class = TemporaryTransactionSerializer


