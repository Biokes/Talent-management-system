from django.urls import path, include

from talent_management_system import views

urlpatterns = [
    path('user/create-user/', views.on_board)
]