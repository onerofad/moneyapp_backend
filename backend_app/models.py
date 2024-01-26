from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    verify = models.IntegerField(default=0)

    def __str__(self):
        return self.fname