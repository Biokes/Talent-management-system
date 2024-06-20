from django.shortcuts import render
from rest_framework.decorators import api_view

from talent_management_system.forms import Apply
from talent_management_system.models import Employee


# Create your views here.

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

# def edit_employee_details(request):
#     form =
#
#
# def delete_employee(request):
#     form =