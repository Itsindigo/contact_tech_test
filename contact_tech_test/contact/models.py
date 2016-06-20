from django.db import models
from django.core import validators

class Contact(models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200, validators=[validators.validate_email])

# Create your models here.
