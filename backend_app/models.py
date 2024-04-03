from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.TextField(default = '')
    dob = models.DateField(default='2024-01-24')
    password = models.CharField(max_length=255)
    verify = models.IntegerField(default=0)

    def __str__(self):
        return self.fname

class ExchangeRates(models.Model):
    country = models.CharField(max_length = 255)
    countrycode = models.CharField(max_length = 255)
    rate = models.IntegerField()
    fee = models.IntegerField(default = 0)

    def __str__(self):
        return self.country
    
class Transactions(models.Model):
    moneySent = models.FloatField()
    moneyReceived = models.FloatField()
    currencySent = models.CharField(max_length = 255, default = '')
    currencyReceived = models.CharField(max_length = 255, default = '' )
    fee = models.FloatField()
    total = models.FloatField()

    deliveryBank = models.BooleanField(default = False)
    deliveryCash = models.BooleanField(default = False)
    zenith = models.BooleanField(default = False)
    gtb = models.BooleanField(default = False)
    polaris = models.BooleanField(default = False)

    accountNumber = models.CharField(max_length = 255)
    retypeAccountNumber = models.CharField(max_length = 255)
    checking = models.BooleanField(default = False)
    savings = models.BooleanField(default = False)

    fname = models.CharField(max_length = 255)
    mname = models.CharField(max_length = 255, default = 'none')
    lname = models.CharField(max_length = 255)
    slname = models.CharField(max_length = 255, default = 'none')
    country = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    street = models.CharField(max_length = 255)
    street2 = models.CharField(max_length = 255, default = 'none' )
    region = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    postal = models.CharField(max_length = 255)

    cardNumber = models.CharField(max_length = 255)
    expiration = models.CharField(max_length = 255)
    securityCode = models.CharField(max_length = 255)
    b_fname = models.CharField(max_length = 255)
    nickname = models.CharField(max_length = 255, default = 'none') 
    streetAd = models.CharField(max_length = 255)
    apartment = models.CharField(max_length = 255,  default = 'none')
    b_city = models.CharField(max_length = 255)
    b_region = models.CharField(max_length = 255)
    zipcode = models.CharField(max_length = 255)

    senderEmail = models.CharField(max_length = 255, default = '')
    trans_date = models.DateField(auto_now = True)

    