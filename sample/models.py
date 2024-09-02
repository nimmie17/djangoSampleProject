from django.db import models

# Create your models here.

class UserNumber(models.Model):
    phone_number = models.CharField(max_length=50)