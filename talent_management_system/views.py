from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from talent_management_system.forms import UpdatePasswordForm, SetGoalForm, PromoteEmployeeForm, DeleteEmployeeForm, \
    GetAllEmployeeProfiles, GetEmployeeProfile, WellBeingForm

from talent_management_system.forms import EmployeeOnboardingForm, ScheduleTrainingForm

from talent_management_system.models import Employee, Goal, PerformanceReview


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
    if request.method == 'PATCH':
        form = UpdatePasswordForm(request.PATCH)
        if form.is_valid:
            employee = form.save(commit=False)
            gotten_id = form.cleaned_data["gotten_id"]
            old_password = form.cleaned_data["password"]
            new_password = form.cleaned_data['new_password']
            employee = authenticate(email=gotten_id, password=old_password)
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
                manager = authenticate(email=form.cleaned_data['boss_email'],
                                       password=form.cleaned_data['boss_password'])
                if manager is None:
                    messages.error(request, 'Invalid manager details.' +
                                   ' Please enter a valid manager details.')
                    return redirect('set_goals_for_employee')
                employee = Employee.objects.get(email=form.cleaned_data['email'])
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

    context = {'form': form}
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


def manage_employee_performance(request):
    if request.method == 'GET':
        form = PerformanceReview(request.GET)
        if form.is_valid():
            try:
                manager_email = form.cleaned_data['manager_email']
                password = form.cleaned_data['password']
                employee_email = form.cleaned_data['employee_email']
                manager = authenticate(email=manager_email, password=password)
                if manager is not None:
                    try:
                        employee = Employee.objects.get(email=employee_email)
                        return render(request, 'employee_performance.html', {'employee': employee, 'form': form})
                    except Employee.DoesNotExist:
                        messages.error(request, 'Employee not found.')
                        return redirect('set_goals_for_employee')
                else:
                    messages.error(request, 'Invalid manager details. Please enter valid manager details.')
                    return redirect('set_goals_for_employee')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
                return redirect('set_goals_for_employee')
    else:
        form = PerformanceReview()

    context = {'form': form}
    return render(request, 'set_goals_for_employee.html', context)


def promote_employee_wellbeing(request):
    if request.method == 'POST':
        form = WellBeingForm(request.POST)
        if form.is_valid():
            try:
                manager = authenticate(email=form.cleaned_data['manager_email'], password=form.cleaned_data['password'])
                if manager is not None:
                    wellbeing_program = form.save()
                    messages.success(request, 'Employee well-being program added successfully.')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid manager details. Please enter valid manager details.')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form = WellBeingForm()
    return render(request, 'promote_employee_wellbeing.html', {'form': form})
