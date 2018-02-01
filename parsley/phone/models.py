from django.db import models

from parsley.patient.models import Patient

class Phone(models.Model):
    MOBILE = 'mobile'
    HOME = 'home'
    OFFICE = 'office'
    TYPE_CHOICES = (
        (MOBILE, 'Mobile'),
        (HOME, 'Home'),
        (OFFICE, 'Office'),
    )

    patient = models.ForeignKey(Patient, related_name='phones', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, blank=True, default=MOBILE)
    number = models.CharField(max_length=20, blank=True)

