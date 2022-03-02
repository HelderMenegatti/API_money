from api.models import CoinsAvailable
from rest_framework import serializers

class CoinsAvailableSerializer(serializers.ModelSerializer):
    """
    API models serialization class converts money
    """
    class Meta:
        model = CoinsAvailable
        fields = [
            'from_coins',
            'to_coins',
            'amount',
        ]
