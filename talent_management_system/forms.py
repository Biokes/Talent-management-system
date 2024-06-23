from django import forms
from talent_management_system.models import Manager, Training, Goal

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


# class UpdatePasswordForm(forms.Form):
#     class Meta:
#         model = Employee
#         fields = ['email', 'password']
#         current_password = forms.CharField(widget=forms.PasswordInput)
#         new_password = forms.CharField(widget=forms.PasswordInput)
#         confirm_password = forms.CharField(widget=forms.PasswordInput)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         new_password = cleaned_data.get("new_password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if new_password != confirm_password:
#             raise forms.ValidationError("New password and confirm password do not match.")
#
#         return cleaned_data
#
#     # class Meta:
#     #     model = Employee
#     #     fields = ['email', 'password']
#     #     widgets = {
#     #         'email': forms.EmailInput(attrs={'placeholder': 'email', 'type': 'text'}),
#     #         'old_password': forms.PasswordInput(attrs={'placeholder': 'old password', 'type': 'password'}),
#     #         'new_password': forms.PasswordInput(attrs={'placeholder': 'new password', 'type': 'password'})
#         }
class UpdatePasswordForm(forms.Form):
    email = forms.EmailField()
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password != confirm_password:
            raise forms.ValidationError("New password and confirm password do not match.")

        return cleaned_data


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
        model = Goal
        fields = ['employee_id', 'start_date', 'end_date', 'description']
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
        fields = ['email', 'password', 'position']

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'email ', 'type': 'text'}),
            'password': forms.TextInput(attrs={'placeholder': 'password', 'type': 'password'}),
            'employee_email': forms.TextInput(attrs={'placeholder': 'staff email', 'type': 'email'}),
            'position': forms.TextInput(attrs={'placeholder': 'POSITION', 'type': 'text'})
        }


class DeleteEmployeeForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['email', 'password']
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
        fields = ['email', 'password']
        widgets = {
            'manager_email': forms.TextInput(attrs={'placeholder': 'email ', 'type': 'text'}),
            'password': forms.TextInput(attrs={'placeholder': 'password', 'type': 'password'}),
            'employee_email': forms.TextInput(attrs={'placeholder': 'Employee email ', 'type': 'text'})
        }

