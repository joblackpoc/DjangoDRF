from django.db import models


COUNTRIES = [
    ("TH", "THAILAND"),
    ("IND", "INDIA"),
    ("USA", "United States of America"),
    ("UK", "United Kingdom"),
    ("AUS", "AUSTRALIA"),
    ("AU", "AUSTRIA"),
    ("SP", "SPAIN"),
]
# Create your models here.
class Employee(models.Model):
    Firtname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Titlename = models.CharField(max_length=50)
    Haspassport = models.BooleanField()
    Salary = models.IntegerField()
    Birthdate = models.DateField()
    Hiredate = models.DateField()
    Notes = models.CharField(max_length=200)
    Country = models.CharField(max_length=50, choices=COUNTRIES, default=None)
    Email = models.EmailField(default="",max_length=60)
    Phonenumber = models.CharField(max_length=20, default="")