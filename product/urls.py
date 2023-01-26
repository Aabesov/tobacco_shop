from django.urls import path
from . import views

urlpatterns = [
    path("get/", views.ProductListAPIView.as_view()),
    path("create/", views.ProductListAPIView.as_view()),
    path("update/<int:pk>/", views.ProductListAPIView.as_view()),
    path("delete/<int:pk>/", views.ProductListAPIView.as_view())
]