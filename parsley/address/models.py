from django.db import models

from parsley.patient.models import Patient

# Create your models here.

class Address(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    line_1 = models.CharField(max_length=254, blank=False, null=False)
    line_2 = models.CharField(max_length=254, blank=True, default='')
    city = models.CharField(max_length=254, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)
    zip = models.CharField(max_length=5, blank=False, null=False)


