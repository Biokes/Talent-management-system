from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from talent_management_system.forms import Apply
from talent_management_system.forms import EmployeeOnboardingForm


@api_view(["POST"])
def on_board(request):
    form = Apply(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        new_employee = authenticate(first_name=first_name, last_name=last_name,
                                    email=email, phone_number=phone_number)
        new_employee = form.save()


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
            user = authenticate(first_name=first_name, last_name=last_name, email=email, password=password,
                                phone_number=phone_number)
            if user is not None:
                form.save()
                login(request, user)
                messages.success(request, 'You have successfully Registered!')
                return redirect('home')
    else:
        form = EmployeeOnboardingForm()
        return render(request, 'onboard_employee.html', {'form': form})


def employee_details(request):
    return render(request, 'onboard_employee.html')
