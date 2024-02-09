from django.contrib import admin
from .models import Register, ExchangeRates, Transactions

admin.site.register({Register, ExchangeRates})