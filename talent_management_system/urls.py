from django.urls import path, include

from talent_management_system import views

urlpatterns = [
    path('user/create-user/', views.on_board)
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_employee/', views.onboard_employee, name='onboard_employee'),
]