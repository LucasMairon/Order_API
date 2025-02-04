from django.db import models

IS_PAYED_CHOICES = {
    'Pago': 'Pago',
    'A pagar': 'A Pagar',
}

class Order(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    entry_time = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(auto_now=True)
    is_payed = models.CharField(max_length=7,choices=IS_PAYED_CHOICES, null=True, blank=True)
    payment_form = models.CharField(max_length=50, null=True, blank=True)

