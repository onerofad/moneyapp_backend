from django.shortcuts import render
from .models import Register
from .serializers import RegisterSerializer
from rest_framework import viewsets

class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer