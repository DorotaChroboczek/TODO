from datetime import date, time

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField, TimeField
from django.forms import *

from .models import *
from accounts.models import Profile


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


class DateInput(DateInput):
    input_type = 'date'


class TimeInput(TimeInput):
    input_type = 'time'


# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('username',)
#
#     username = CharField(widget=TextInput(attrs={'placeholder': 'Name...'}),
#                          max_length=50)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('member', 'title', 'date', 'time')

    title = CharField(max_length=250)
    date = FutureDateField()
    time = FutureTimeField()

    # def __init__(self, person=None, **kwargs):
    #     super().__init__(**kwargs)
    #     if person:
    #         self.fields['member'].queryset = MembersGroup.objects.filter(person=person)

    # person = ModelChoiceField(queryset=MembersGroup.objects.filter(person=person).all())

