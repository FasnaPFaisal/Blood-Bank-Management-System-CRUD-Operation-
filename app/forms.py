from django import forms
from .models import Donate

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }