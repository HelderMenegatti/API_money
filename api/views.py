import json
import requests
from api.serializers import CoinsAvailableSerializer
from rest_framework import generics
from rest_framework.response import Response



class ConvertCurrencies(generics.CreateAPIView):
    """
    This class is used to convert the amount of a given currency pair
    """
    serializer_class = CoinsAvailableSerializer
    def post(self, request, *args, **kwargs):
        try:
            body = json.loads(request.body)
        except:
            body = self.request.POST

        fr = body['from_coins']
        to = body['to_coins']
        amount = float(body['amount'])
        url = f'https://economia.awesomeapi.com.br/json/last/{fr}-{to}'
        title_dict = fr + to
        api = requests.get(url=url)
        api_json = api.json()
        try:
            count = amount*float(api_json[title_dict]['ask'])
            data = {
                'from': fr,
                'to': to,
                'amount': amount,
                'result': "%.2f" % count,
            }
            return Response(data)
        except KeyError:
            return Response(api_json)
