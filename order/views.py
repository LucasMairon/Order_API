from .models import Order
from .serializer import OrderModelSerializer
from rest_framework import viewsets
from rest_framework import filters

class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', '=is_payed',]
