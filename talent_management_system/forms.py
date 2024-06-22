from django import forms
from talent_management_system.models import Manager, Training, Goal, WellBeingProgram

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


class UpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'email', 'type': 'text'}),
            'old_password': forms.PasswordInput(attrs={'placeholder': 'old password', 'type': 'password'}),
            'new_password': forms.PasswordInput(attrs={'placeholder': 'new password', 'type': 'password'})
        }


class EmployeeTrainingForm(forms.ModelForm):
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
            'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number', 'type': 'number'})
        }


class SetGoalForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['boss_email', 'boss_password', 'start_date', 'end_date', 'description', 'name']
        widgets = {
            'boss_email': forms.TextInput(attrs={'placeholder': 'email', 'type': 'text'}),
            'boss_password': forms.TextInput(attrs={'placeholder': 'password', 'type': 'password'}),
            'email': forms.TextInput(attrs={'placeholder': 'email', 'type': 'email'}),
            'start_date': forms.TextInput(attrs={'placeholder': 'goal start date', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'placeholder': 'goal end date', 'type': 'date'}),
            'description': forms.TextInput(attrs={'placeholder': 'Goal description', 'type': 'text'})
        }


class PromoteEmployeeForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['email', 'password', 'employee_email', 'position']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'email ', 'type': 'text'}),
            'password': forms.TextInput(attrs={'placeholder': 'password', 'type': 'password'}),
            'employee_email': forms.TextInput(attrs={'placeholder': 'staff email', 'type': 'email'}),
            'position': forms.TextInput(attrs={'placeholder': 'POSITION', 'type': 'text'})
        }


class DeleteEmployeeForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['email', 'password', 'employee_email']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'email ', 'type': 'text'}),
            'password': forms.TextInput(attrs={'placeholder': 'password', 'type': 'password'}),
            'employee_email': forms.TextInput(attrs={'placeholder': 'staff email', 'type': 'email'})
        }


class GetAllEmployeeProfiles(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'email ', 'type': 'text'}),
            'password': forms.TextInput(attrs={'placeholder': 'password', 'type': 'password'}),
        }


class GetEmployeeProfile(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['email', 'password', 'employee_email']
        widgets = {
            'manager_email': forms.TextInput(attrs={'placeholder': 'email ', 'type': 'text'}),
            'password': forms.TextInput(attrs={'placeholder': 'password', 'type': 'password'}),
            'employee_email': forms.TextInput(attrs={'placeholder': 'Employee email ', 'type': 'text'}),

        }


class WellBeingForm(forms.ModelForm):
    manager_email = forms.EmailField(label='Manager Email', max_length=100)
    password = forms.CharField(label='Manager Password', widget=forms.PasswordInput)
    title = forms.CharField(label='Program Title', max_length=100)
    description = forms.CharField(label='Program Description', widget=forms.Textarea)
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.CharField(label='Location', max_length=100)

    class Meta:
        model = WellBeingProgram
        fields = ['manager_email', 'password', 'title', 'description', 'start_date', 'end_date', 'location']

