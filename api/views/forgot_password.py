
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from api.serializers.forgot_password import ForgotPasswordSerializer
from api.utils import send_otp
from api.helper import generate_token
from django.conf import settings

# Get the custom User model
User = get_user_model()

# API endpoint for handling forgot password requests
class ForgotPasswordAPIView(APIView):
    def post(self, request):
        # Validate the incoming email
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                # Try to find the user by email
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # If not found, return 404
                return Response({'detail': 'Email not found or registered.'}, status=status.HTTP_404_NOT_FOUND)

            # Generate a secure token for password reset
            token = generate_token(user.id, user.email)
            user.token = token
            user.save()

            # Build the reset link for the frontend
            reset_link = f"http://localhost:3011/reset-password/{token}"

            # Send the reset link to the user's email
            send_otp(
                email_subject='Password Reset Request',
                email_template='email_verification.html',
                recipient_email=email,
                context={'reset_link': reset_link, 'user': user}
            )
            # Respond with success
            return Response({'detail': 'A reset link has been sent to your email.'}, status=status.HTTP_200_OK)
        # If serializer is invalid, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
