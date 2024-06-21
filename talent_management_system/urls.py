from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_employee/', views.onboard_employee, name='onboard_employee'),
]