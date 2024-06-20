from django import forms

from talent_management_system.models import Employee


class Apply(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']
        widgets = {
            'first_name': (forms.TextInput(attrs={'placeholder': 'first name'})),
            'last_name': (forms.TextInput(attrs={'placeholder': 'last name'})),
            'email': (forms.TextInput(attrs={"placeholder": 'Email', 'type': 'email'})),
            'password': (forms.PasswordInput(attrs={'placeholder': 'password'})),
            'phone_number': (forms.TextInput(attrs={"placeholder": 'Phone number', 'type': 'number'}))
        }
