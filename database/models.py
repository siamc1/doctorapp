from django.db import models
import csv

class Patient(models.Model):
    name = models.CharField(max_length = 30)
    DOB = models.DateTimeField()
    sex = models.CharField(max_length = 10)
    blood_pressure = models.CharField(max_length = 10)
    risk_factor = models.FloatField()

with open("csv/Tony.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Patient.objects.get_or_create(
            name=row[0],
            risk_factor=row[1],
            sex=row[3],
            blood_pressure=row[4],
            DOB=row[5],
        )
