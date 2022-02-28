from api.models import CoinsAvailable
from rest_framework import serializers

class CoinsAvailableSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoinsAvailable
        fields = [
            'from_coins',
            'to_coins',
            'amount',
        ]
