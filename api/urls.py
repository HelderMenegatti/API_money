from django import views
from django.urls import path, include
from api.views import ConvertCurrencies
from rest_framework.routers import DefaultRouter 


urlpatterns = [
    path('api/', ConvertCurrencies.as_view(), name="get_value")
]