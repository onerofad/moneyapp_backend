from rest_framework import serializers
from .models import Accounts

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Accounts
