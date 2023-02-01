from django.urls import path
from . import views
from .views import LoginJWTView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("register/", views.RegisterUserAPIView.as_view()),
    path("logout/", views.UserTokenLogoutAPIView.as_view()),
    path("activate/<str:activation_code>/", views.ActivateAccountView.as_view(), name="activate_account"),
    path("password_change/", views.PasswordChangeView.as_view()),
    path('login/', LoginJWTView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('favorite/', views.FavoriteAPIView.as_view()),
]
