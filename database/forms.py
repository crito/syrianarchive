from django import forms
from models import LocationPlace, ViolationType

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