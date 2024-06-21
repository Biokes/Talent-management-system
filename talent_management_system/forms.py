from django import forms
from talent_management_system.models import Employee, Manager, Training

from talent_management_system.models import Employee


class EmployeeOnboardingForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
            'phone_number'
            : forms.TextInput(
                attrs={'placeholder': 'Phone number', 'type': 'number', 'class': 'form-control'})
        }


class UpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['email', 'old_password', 'new_password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'email', 'type': 'text'}),
            'old_password': forms.PasswordInput(attrs={'placeholder': 'old password', 'type': 'password'}),
            'new_password': forms.PasswordInput(attrs={'placeholder': 'new password', 'type': 'password'})
        }
class EmployeeTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['title', 'description', 'start_date', 'end_date', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': 'description', 'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'placeholder': 'start date (YYYY-MM-DD)', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'end date (YYYY-MM-DD)', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'Training location', 'class': 'form-control'})
        }


class ManagerOnboardingForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number', 'type': 'number'})
        }
