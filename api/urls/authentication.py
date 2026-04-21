from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api.views import(
    SignUpEndpoint,
    SignInEndPoint,
    ForgotPasswordEndpoint,
    ResetPasswordEndpoint
)

urlpatterns = [
    path('user/sign-up/', SignUpEndpoint().as_view()),
    path('user/sign-in/', SignInEndPoint().as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path('user/forgot-password/', ForgotPasswordEndpoint.as_view()),
    path('user/reset-password/', ResetPasswordEndpoint.as_view()),
]
