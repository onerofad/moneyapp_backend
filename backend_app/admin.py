from django.contrib import admin
from .models import Register, ExchangeRates

admin.site.register({Register, ExchangeRates})