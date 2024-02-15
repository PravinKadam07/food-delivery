# delivery_system/urls.py
from django.urls import path
from .views import PricingDetail

urlpatterns = [
    path('<int:pk>/', PricingDetail.as_view(), name='pricing-detail'),
]
