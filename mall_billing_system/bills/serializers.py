from rest_framework import serializers
from .models import Bill
from products.serializers import ProductSerializer

class BillSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ['id', 'customer', 'products', 'total_amount', 'date']
