from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length = 30)
    DOB = models.DateTimeField()
    sex = models.CharField(max_length = 10)
    blood_pressure = models.CharField(max_length = 10)
    risk_factor = models.FloatField()
