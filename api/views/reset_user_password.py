from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from db.models import User
from api.utils import send_otp

# Base URL for the frontend application
FRONTEND_BASE_URL = getattr(settings, "FRONTEND_BASE_URL", "http://localhost:3011")


# ForgotPasswordEndpoint sends a generated token to the user's email
class ForgotPasswordEndpoint(APIView):
    def post(self, request):
        # validate email exists
        email = request.data.get("email", "").strip()
        if not email:
            return Response({"message": "Email is required.", "statusCode": 400})

        try:
            # get user by email
            user = User.objects.get(email=email)

            # generates uid and token for password reset link
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = f"{FRONTEND_BASE_URL}/reset-password?uid={uid}&token={token}"

            # sends password reset email
            send_otp(
                email_subject="Reset Your CS Pro Plane Password",
                email_template="reset_user_password.html",
                recipient_email=user.email,
                context={
                    "reset_url": reset_url,
                    "recipient_email": user.email,
                },
            )
        # if email doesn't exist, do nothing
        except User.DoesNotExist:
            pass
        except Exception as e:
            print("ForgotPasswordEndpoint error:", e)

        return Response(
            {
                "message": "If an account with that email exists, a reset link has been sent.",
                "statusCode": 200,
            }
        )


# ResetPasswordEndpoint validates the token and resets the user's password
class ResetPasswordEndpoint(APIView):
    def post(self, request):
        # validate uid, token, and new_password are provided
        uid = request.data.get("uid", "")
        token = request.data.get("token", "")
        new_password = request.data.get("new_password", "")
        if not uid or not token or not new_password:
            return Response(
                {
                    "message": "uid, token, and new_password are all required.",
                    "statusCode": 400,
                }
            )

        # lookup user by uid
        try:
            user_pk = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_pk)
        except (User.DoesNotExist, ValueError, OverflowError, Exception) as e:
            print("ResetPasswordEndpoint - user lookup error:", e)
            return Response(
                {
                    "message": "Invalid or expired reset link.",
                    "statusCode": 400,
                }
            )

        # validate the token is valid for the user
        if not default_token_generator.check_token(user, token):
            return Response(
                {
                    "message": "Reset link is invalid or has expired.",
                    "statusCode": 400,
                }
            )

        # validate password length
        if len(new_password) < 6:
            return Response(
                {
                    "message": "Password must be at least 6 characters.",
                    "statusCode": 400,
                }
            )

        # hash the new password and save it to the user
        user.password = make_password(new_password)
        user.save()

        return Response(
            {
                "message": "Password reset successfully. You can now sign in.",
                "statusCode": 200,
            }
        )
