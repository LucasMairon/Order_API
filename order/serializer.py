from .models import Order
from rest_framework import serializers

class OrderModelSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Order
        fields = '__all__'
