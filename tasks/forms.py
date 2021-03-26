from datetime import date, time

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField, TimeField
from django.forms import *

from .models import *


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized')


def capitalize_value(value):
    if value[0].islower():
        value[0].capitalize()
    return value

