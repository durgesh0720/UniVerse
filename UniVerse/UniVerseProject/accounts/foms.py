from django import forms
from .models import student_registration

class DoB(forms.ModelForm):
    class Meta:
        model = student_registration
        fields = ['date_of_birth']  # List fields you want to include
    date_of_birth = forms.DateField(required=False, input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}))
