from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from talent_management_system.forms import UpdatePasswordForm, SetGoalForm, PromoteEmployeeForm, DeleteEmployeeForm, \
    GetAllEmployeeProfiles, GetEmployeeProfile

from talent_management_system.forms import EmployeeOnboardingForm, ScheduleTrainingForm

from talent_management_system.models import Employee, Goal, Manager
from .models import Staff


def home(request):
    return render(request, 'home.html')


def onboard_employee(request):
    if request.method == 'GET':
        form = EmployeeOnboardingForm()
        return render(request, 'onboard_employee.html', {'form': form})
    elif request.method == 'POST':
        form = EmployeeOnboardingForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            if Employee.objects.filter(email=email).exists():
                messages.error(request, 'User already exists!')
                return render(request, 'onboard_employee.html', {'form': form})
            Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                phone_number=phone_number
            )
            messages.success(request, 'You have successfully registered!')
            return redirect('update_password')
        else:
            messages.error(request, 'There was an error with your submission.')
    return render(request, 'onboard_employee.html', {'form': form})


def employee_details(request):
    return render(request, 'onboard_employee.html')


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


def update_password(request):
    if request.method == 'GET':
        form = UpdatePasswordForm()
        return render(request, 'update_employee_password.html', {'form': form})
    elif request.method == 'POST':
        form = UpdatePasswordForm(request.POST)
        if form.is_valid:
            messages.success(request, 'form is updated')
            email = form['email']
            old_password = form['current_password']
            new_password = form['new_password']
            confirm_new = form['confirm_password']
            if confirm_new is not new_password:
                messages.success(request, 'Password did not match')
            employee = authenticate(email=new_password, password=old_password)
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
    return render(request, 'home.html', {'form': form})


def promote_employee(request):
    if request.method == 'PATCH':
        form = PromoteEmployeeForm(request.PATCH)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                employee_email = form.cleaned_data['employee_email']
                position = form.cleaned_data['position']
                manager = authenticate(email=email, password=password)
                if manager is not None:
                    employee = Employee.objects.get(email=employee_email)
                    employee.position = position.upper()
                    employee.save()
                else:
                    messages.error(request, 'Invalid manager details. Please enter a valid manager details.')
                    return redirect('set_goals_for_employee')
            except Exception:
                messages.error(request, 'An error occured.')
                return redirect('set_goals_for_employee')


def set_goals_for_employee(request):
    if request.method == 'POST':
        form = SetGoalForm(request.POST)
        if form.is_valid():
            try:
                manager = Manager.objects.get(email=form.cleaned_data['boss_email'],
                                              password=form.cleaned_data['boss_password'])
                if manager is None:
                    messages.error(request, 'Invalid manager details.' +
                                   ' Please enter a valid manager details.')
                    return redirect('set_goals_for_employee')
                employee = Employee.objects.get(email=form.cleaned_data['email'])
                if employee is None:
                    messages.error(request, 'Invalid manager details.' +
                                   ' Please enter a valid manager details.')
                    return redirect('set_goals_for_employee')
                goal = Goal.objects.create(
                    employee=employee.employee_id,
                    start_date=form.cleaned_data['start_date'],
                    end_date=form.cleaned_data['end_date'],
                    description=form.cleaned_data['description']
                )
                goal.save()
                return messages.success(request, "successful")
            except Employee.DoesNotExist:
                messages.error(request, 'Invalid employee ID. Please enter a valid ID.')
                return redirect('set_goals_for_employee')

    else:
        form = SetGoalForm()

    context = {'form': form}
    return render(request, 'set_goals_for_employee.html', context)


def search_for_all_employees(request):
    if request.method == 'GET':
        form = GetAllEmployeeProfiles(request.GET)
        context = {'form': form}
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                manager = authenticate(email=email, password=password)
                if manager is not None:
                    employees = Employee.objects.all()
                    return render('', employees, {'form': form})
                else:
                    messages.error(request, 'Invalid manager details. Please enter a valid manager details.')
                    return redirect('set_goals_for_employee')
            except Exception:
                messages.error(request, 'An error occured.')
                return redirect('set_goals_for_employee')

    return render(request, 'set_goals_for_employee.html', context)


def delete_employee(request):
    if request.method == 'DELETE':
        form = DeleteEmployeeForm(request.DELETE)
        context = {'form': form}
        if form.is_valid():
            try:
                manager = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'], )
                if manager is None:
                    messages.error(request, 'Invalid Details provided.')
                    return render(request, 'set_goals_for_employee.html', context)
                gotten_employee = Employee.objects.get(email=form.cleaned_data['employee_email'])
                if gotten_employee is None:
                    messages.error(request, 'Invalid Details provided.')
                    return render(request, 'set_goals_for_employee.html', context)
                gotten_employee.delete()
                messages.success(request, "deleted successfully")
            except Exception:
                messages.error(request, 'Invalid Details provided.')
                return render(request, 'set_goals_for_employee.html', context)

    else:
        form = SetGoalForm()

    context = {'form': form}
    return render(request, 'set_goals_for_employee.html', context)


def search_employee_profiles(request):
    if request.method == 'GET':
        form = GetEmployeeProfile(request.GET)
        if form.is_valid():
            try:
                manager_email = form.cleaned_data['manager_email']
                password = form.cleaned_data['password']
                employee_email = form.cleaned_data['employee_email']
                manager = authenticate(email=manager_email, password=password)
                if manager is not None:
                    employees = Employee.objects.get(email=employee_email)
                    return render('', employees, {'form': form})
                else:
                    messages.error(request, 'Invalid manager details. Please enter a valid manager details.')
                    return redirect('set_goals_for_employee')
            except Exception:
                messages.error(request, 'An error occured.')
                return redirect('set_goals_for_employee')
    context = {'form': form}
    return render(request, 'set_goals_for_employee.html', context)

# def manage_employee_performance(request):
#     if request.method == 'GET':
#         form = PerformanceReview(request.GET)
#         if form.is_valid():
#             try:
#                 manager_email = form.cleaned_data['manager_email']
#                 password = form.cleaned_data['password']
#                 employee_email = form.cleaned_data['employee_email']
#                 manager = authenticate(email=manager_email, password=password)
#                 if manager is not None:
#                     employees = Employee.objects.get(email=employee_email)
#                     return render('', employees, {'form': form})
#                 else:
#                     messages.error(request, 'Invalid manager details. Please enter a valid manager details.')
#                     return redirect('set_goals_for_employee')
#             except Exception:
#                 messages.error(request, 'An error occured.')
#                 return redirect('set_goals_for_employee')
#
#     context = {'form': form}
#     return render(request, 'set_goals_for_employee.html', context)
