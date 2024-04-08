from django.shortcuts import render
from rest_framework import generics
from .models import Bill
from .serializers import BillSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bill
from mall_billing_system.bills import models

class AnalyticsAPIView(APIView):
    def get(self, request):
        # Total sales by customer
        total_sales_by_customer = Bill.objects.values('customer__name').annotate(total_sales=models.Sum('total_amount')).order_by('-total_sales')

        # Top selling products
        top_selling_products = Bill.objects.values('products__name').annotate(total_sold=models.Sum('products__quantity')).order_by('-total_sold')

        # Total sales over a specific period (e.g., last 30 days)
        from django.utils import timezone
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        total_sales_last_30_days = Bill.objects.filter(date__gte=thirty_days_ago).aggregate(total_sales=models.Sum('total_amount'))

        analytics_data = {
            'total_sales_by_customer': total_sales_by_customer,
            'top_selling_products': top_selling_products,
            'total_sales_last_30_days': total_sales_last_30_days['total_sales'] if total_sales_last_30_days['total_sales'] else 0,
        }

        return Response(analytics_data)


class BillListView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

# Create your views here.
