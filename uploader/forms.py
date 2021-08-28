from django import forms
from .models import Resume

CITY_CHOICES = [
    ('Lahore', 'Lahore'),
    ('Faisalaabad', 'Faisalaabad'),
    ('Rawalpindi', 'Rawalpindi'),
    ('Multan', 'Multan'),
    ('Bahawalpur','Bahawalpur')
]

class ResumeForm(forms.ModelForm):
    job_city = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=CITY_CHOICES)
    class Meta:
        model = Resume
        fields = '__all__'
        labels = {'job_city':'Job City'}
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'father_name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.NumberInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'file': forms.FileInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'gender': forms.RadioSelect()
        }
