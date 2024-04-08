from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    # Add more URL patterns for authentication, updating employee details, etc.
]
