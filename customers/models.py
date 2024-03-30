from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_format(number):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pattern.match(number):
        return True
    else:
        raise ValidationError(
            _('%(number)s is incorrect phone number format'),
            params={'number':number},
        )


# Create your models here.
class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15, validators=[validate_format])
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=20)
    postalcode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  # auto generate date time stamp    

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

