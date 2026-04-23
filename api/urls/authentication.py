from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

# Import authentication and password reset views
from api.views import(
    SignUpEndpoint,
    SignInEndPoint
)
from api.views.forgot_password import ForgotPasswordAPIView
from api.views.reset_password import ResetPasswordAPIView

# Define URL patterns for authentication and password reset
urlpatterns = [
    # User registration endpoint
    path('user/sign-up/', SignUpEndpoint().as_view()),
    # User login endpoint
    path('user/sign-in/', SignInEndPoint().as_view()),
    # JWT token refresh endpoint
    path("token/refresh/", TokenRefreshView.as_view()),

    # Forgot password endpoint
    path('user/forgot-password/', ForgotPasswordAPIView.as_view()),

    # Reset password endpoint
    path('user/reset-password/', ResetPasswordAPIView.as_view()),
]
