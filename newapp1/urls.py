from django.contrib import admin
from django.urls import path,include
from .views import EmployeesView

urlpatterns = [
path('',EmployeesView.as_view()),
path('<int:e_id>/',EmployeesView.as_view()),
]