from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view

from talent_management_system.forms import EmployeeOnboardingForm
from talent_management_system.models import Employee


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
            user = authenticate(first_name=first_name, last_name=last_name, email=email, password=password, phone_number=phone_number)
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
