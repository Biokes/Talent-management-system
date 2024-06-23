from django.urls import path

from talentManagement import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_employee/', views.onboard_employee, name='onboard_employee'),
    path('schedule_training/', views.schedule_training, name='schedule_training')
]
