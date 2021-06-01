from django.urls import path
from . import views

urlpatterns = [
    path("<plate_or_vin>", views.get_car_data),
]
