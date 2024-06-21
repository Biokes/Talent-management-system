from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from talent_management_system.forms import UpdatePasswordForm, SetGoalForm

from talent_management_system.forms import EmployeeTrainingForm
from talent_management_system.forms import EmployeeOnboardingForm

from talent_management_system.models import Employee, Goal


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
                user = authenticate(first_name=first_name, last_name=last_name, email=email,
                                    password=password, phone_number=phone_number)
                if user is not None:
                    form.save()
                    login(request, employee)
                    messages.success(request, 'You have successfully Registered!')
                    return redirect('home')
        else:
            form = EmployeeOnboardingForm()
            return render(request, 'onboard_employee.html', {'form': form})


def employee_details(request):
    return render(request, 'onboard_employee.html')


def update_password(request):
    if request.method == 'PATCH':
        form = UpdatePasswordForm(request.PATCH)
        if form.is_valid:
            employee = form.save(commit=False)
            id = form.cleaned_data["id"]
            old_password = form.cleaned_data["password"]
            new_password = form.cleaned_data['new_password']
            employee = authenticate(email=id, password=old_password)
            if employee is not None:
                employee.password = new_password
                employee.save()
                messages.success(request, 'Successfully Updated')
                return redirect('home')
            else:
                messages.success(request, 'Invalid Details')
    else:
        form = UpdatePasswordForm()
        return render(request, 'update_employee_password.html', {'form': form})


def take_training(request):
    if request.method == 'POST':
        form = EmployeeTrainingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            location = form.cleaned_data['location']


def set_goals_for_employee(request):
    if request.method == 'POST':
        form = SetGoalForm(request.POST)
        if form.is_valid.save():
            try:
                employee = Employee.objects.get(email=form.cleaned_data['email'])
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                description = form.cleaned_data['description']
                employee_id = employee.employee_id
                goal = Goal.objects.create(
                                            employee=employee,
                                            start_date=form.cleaned_data['start_date'],
                                            end_date=form.cleaned_data['end_date'],
                                            description=form.cleaned_data['description']
                                            )
            except Employee.DoesNotExist:
                messages.error(request, 'Invalid employee ID. Please enter a valid ID.')
                return redirect('set_goals_for_employee')

    else:
        form = SetGoalForm()

    context = {'form': form}
    return render(request, 'set_goals_for_employee.html', context)
