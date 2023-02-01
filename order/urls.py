from django.urls import path
from . import views

urlpatterns = [
    path("create/order/", views.CreateOrderAPIView.as_view())
]