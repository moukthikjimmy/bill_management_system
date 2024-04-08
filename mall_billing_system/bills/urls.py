from django.urls import path
from . import views

urlpatterns = [
    path('bills/', views.BillListView.as_view(), name='bill-list'),
    path('bills/<int:pk>/', views.BillDetailView.as_view(), name='bill-detail'),
    # Add more URL patterns for creating bills, updating bill details, etc.
]
