from django import forms
import datetime

from .models import *
'''
class ProvinceForm(ModelForm):
    class Meta:
        model = LocationPlace

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields['provinces'] =  ModelChoiceField(queryset=LocationPlace.objects.all()),
                                             empty_label="Choose a Province",)



class ViolationForm(ModelForm):
    class Meta:
        model = ViolationType

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields['violations'] =  ModelChoiceField(queryset=ViolationType.objects.all()),
                                             empty_label="Choose a Violation Type",)

'''

class DatabaseFilterForm(forms.ModelForm):
    # add extra fields that you want
    #startDate = forms.DateField(initial=datetime.date.today)
    #endDate = forms.DateField(initial=datetime.date.today)
    #page = forms.IntegerField(initial=1)
    # add the fields from the models
    class Meta:
        model = DatabaseEntry
        fields = ('type_of_violation', 'location')