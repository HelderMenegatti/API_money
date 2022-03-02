from random import choices
from django.db import models
from django.forms import ChoiceField


class CoinsAvailable(models.Model):
    """
    API request pattern template
    """
    COINS_CHOICES = [
        ('EUR', 'Euro'),
        ('USD', 'Dólar'),
        ('BRL', 'Real'),
        ('GBP', 'Libra'),
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum')
    ]

    from_coins = models.CharField(max_length=10, choices=COINS_CHOICES, null=True, blank=True)
    to_coins = models.CharField(max_length=10, choices=COINS_CHOICES, null=True, blank=True)
    amount = models.FloatField()

    def __str__(self):
        return self.id

