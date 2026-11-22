from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # used for automatic password authentication only, customer_id copied to username
    customer_id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=1)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_initial}."