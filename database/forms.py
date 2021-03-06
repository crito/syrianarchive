from django import forms
from datetime import datetime, date
from .models import *

class DatabaseFilterForm(forms.ModelForm):
    # add extra fields that you want
    startDate = forms.DateField(
        required = False,
        initial = datetime.today(),
        widget = forms.DateInput(attrs={'class': 'datepicker'}),
        input_formats = ['%d-%m-%Y','%d %b %Y',],
        )
    endDate = forms.DateField(
        required = False,
        initial = datetime.today(),
        widget = forms.DateInput(attrs={'class': 'datepicker'}),
        input_formats = ['%d-%m-%Y','%d %b %Y',],
        )
    # add the fields from the models
    class Meta:
        model = DatabaseEntry
        fields = ('type_of_violation', 'location')

class MapFilterForm(forms.ModelForm):
    # add extra fields that you want
    startDate = forms.DateField(
        required = False,
        initial = datetime.today(),
        widget = forms.DateInput(attrs={'class': 'datepicker'}),
        input_formats = ['%d-%m-%Y','%d %b %Y',],
        )
    endDate = forms.DateField(
        required = False,
        initial = datetime.today(),
        widget = forms.DateInput(attrs={'class': 'datepicker'}),
        input_formats = ['%d-%m-%Y','%d %b %Y',],
        )
    # add the fields from the models
    class Meta:
        model = DatabaseEntry
        fields = ('type_of_violation',)