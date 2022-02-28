from django import views
from django.urls import path, include
from api.views import ConvertCurrencies
from rest_framework.routers import DefaultRouter 


# router = DefaultRouter()
# router.register(r'api/coin', ConvertCurrencies)

urlpatterns = [
    # path('', include(router.urls)),
    path('api/', ConvertCurrencies.as_view(), name="get_value")
]