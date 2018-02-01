from django.db import models

# Create your models here.
class Patient(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )

    ACTIVE = 'active'
    INACTIVE = 'inactive'
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    )

    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    middle_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank=False, choices=GENDER_CHOICES, default=FEMALE)
    status = models.CharField(max_length=20, blank=False, choices=STATUS_CHOICES, default=ACTIVE)
    terms_accepted = models.BooleanField(default=False)
    terms_accepted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


