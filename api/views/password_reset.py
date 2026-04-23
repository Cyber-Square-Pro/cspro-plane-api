from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils import send_otp
from db.models import User


class ForgotPasswordEndpoint(APIView):
    def post(self, request):
        email = request.data.get("email", "").strip().lower()

        if not email:
            return Response({"message": "Email is required.", "statusCode": 400})

        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = (
                f"{settings.FRONTEND_BASE_URL}/reset-password"
                f"?uid={uid}&token={token}"
            )

            send_otp(
                email_subject="Reset Your CS Pro Plane Password",
                email_template="password_reset.html",
                recipient_email=user.email,
                context={
                    "reset_url": reset_url,
                    "recipient_email": user.email,
                },
            )
        except User.DoesNotExist:
            pass
        except Exception as error:
            print("ForgotPasswordEndpoint error:", error)

        return Response(
            {
                "message": "If an account with that email exists, a reset link has been sent.",
                "statusCode": 200,
            }
        )


class ResetPasswordEndpoint(APIView):
    def post(self, request):
        uid = request.data.get("uid", "")
        token = request.data.get("token", "")
        new_password = request.data.get("new_password", "")

        if not uid or not token or not new_password:
            return Response(
                {
                    "message": "uid, token, and new_password are required.",
                    "statusCode": 400,
                }
            )

        try:
            user_pk = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_pk)
        except Exception as error:
            print("ResetPasswordEndpoint user lookup error:", error)
            return Response(
                {
                    "message": "Invalid or expired reset link.",
                    "statusCode": 400,
                }
            )

        if not default_token_generator.check_token(user, token):
            return Response(
                {
                    "message": "Reset link is invalid or has expired.",
                    "statusCode": 400,
                }
            )

        if len(new_password) < 8:
            return Response(
                {
                    "message": "Password must be at least 8 characters.",
                    "statusCode": 400,
                }
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {
                "message": "Password reset successfully. You can now sign in.",
                "statusCode": 200,
            }
        )
