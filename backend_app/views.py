from django.shortcuts import render
from .models import Accounts
from .serializers import AccountSerializer
from rest_framework import viewsets

class AccountView(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer