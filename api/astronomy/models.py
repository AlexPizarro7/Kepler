from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_ID = models.IntegerField(primary_key = True)