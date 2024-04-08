from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    # Add more URL patterns for adding, updating, or deleting customers.
]
