from django.db import models

# Create your models here.

class Trade(models.Model):
    TRADE_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    date = models.DateField()
    type = models.CharField(max_length=4, choices=TRADE_TYPE_CHOICES)
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    exit_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2)
    strategy = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} on {self.date}"
