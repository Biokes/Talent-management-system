from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from talent_management_system.forms import EmployeeOnboardingForm, ScheduleTrainingForm
from talent_management_system.models import Employee
from talent_management_system.forms import EmployeeOnboardingForm


def home(request):
    return render(request, 'home.html')


def onboard_employee(request):
    if request.method == 'POST':
        form = EmployeeOnboardingForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            phone_number = form.cleaned_data.get('phone_number')
            employee = authenticate(first_name=first_name, last_name=last_name, email=email, password=password,
                                    phone_number=phone_number)
            if employee is not None:
                form.save()
                employee.save()
                login(request, employee)
                messages.success(request, 'You have successfully Registered!')
                return redirect('home')
        else:
            form = EmployeeOnboardingForm()
            return render(request, 'onboard_employee.html', {'form': form})


def employee_details(request):
    return render(request, 'onboard_employee.html')


@api_view()
def schedule_training(request):
    if request.method == 'POST':
        form = ScheduleTrainingForm(request.POST)
        if form.is_valid():
            manager_email = form.cleaned_data['manager_email']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            location = form.cleaned_data['location']
            training = (authenticate
                        (manager_email=manager_email, title=title, description=description, start_date=start_date,
                         end_date=end_date, location=location))
            if training is not None:
                form.save()
                training.save()
                messages.success(request, 'Training scheduled')
                return redirect('home')
        else:
            form = ScheduleTrainingForm()
            return render(request, 'schedule_training.html', {'form': form})
