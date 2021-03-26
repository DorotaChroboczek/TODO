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


class FutureDateField(DateField):

    def validate(self, value):
        super().validate(value)
        if value <= date.today():
            raise ValidationError('Only future dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class FutureTimeField(TimeField):

    def validate(self, value):
        super().validate(value)
        if value <= time():
            raise ValidationError('Only future time allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return time(hour=result.hour, minute=result.minute, second=result.second)

