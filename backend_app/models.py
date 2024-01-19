from django.db import models

class Accounts(models.Model):
    email = models.CharField(max_length=255)