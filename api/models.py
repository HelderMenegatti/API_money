from random import choices
from django.db import models
from django.forms import ChoiceField


class CoinsAvailable(models.Model):
    COINS_CHOICES = [
        ('EUR', 'Euro'),
        ('USD', 'Dolar'),
        ('BRL', 'Real'),
        ('GBP', 'Libra')
    ]

    from_coins = models.CharField(max_length=10, choices=COINS_CHOICES, null=True, blank=True)
    to_coins = models.CharField(max_length=10, choices=COINS_CHOICES, null=True, blank=True)
    amount = models.FloatField()

    def __str__(self):
        return f'{self.from_coins}--{self.to_coins}--{self.amount}'

