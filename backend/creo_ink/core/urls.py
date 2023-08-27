from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import OwnUserDataView, SignupView, UserLoginView, SettingsDataView

urlpatterns = [
    # Other URL patterns
    path("personal/user/", OwnUserDataView.as_view(), name="user_data"),
    path("personal/settings/", SettingsDataView.as_view(), name="user_settings"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
