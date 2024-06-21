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


class ScheduleTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['manager_email', 'title', 'description', 'start_date', 'end_date', 'location']
        widgets = {
            'manager_email': forms.TextInput(attrs={'placeholder': 'manager_email', 'class': 'form-control'}),
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
            'first_name': forms.TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Phone number', 'type': 'number', 'class': 'form-control'})
        }
