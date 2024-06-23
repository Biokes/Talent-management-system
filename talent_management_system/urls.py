from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_employee/', views.onboard_employee, name='onboard_employee'),
    path('schedule_training/', views.schedule_training, name='schedule_training'),
    path('update_password/', views.update_password, name='update_password'),
    path('get_all_employees/', views.search_for_all_employees, name='search_for_all_employees')
]
