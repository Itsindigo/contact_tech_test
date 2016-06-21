from django.db import models
from django.core import validators

class ContactType(models.Model):
    _type = models.CharField(max_length=50, default='General Enquiry')

class Contact(models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200, validators=[validators.validate_email])
    contact_content = models.TextField(default='')
    enquiry_type = models.ForeignKey(ContactType, null=True)


# Create your models here.
