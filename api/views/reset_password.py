from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from api.serializers.reset_password import ResetPasswordSerializer
import jwt
from django.conf import settings

# Get the custom User model
User = get_user_model()

# API endpoint for handling password reset
class ResetPasswordAPIView(APIView):
    def post(self, request):
        # Validate the incoming token and new password
        serializer = ResetPasswordSerializer(data=request.data)
        if not serializer.is_valid():
            # Return detailed serializer errors (e.g., missing fields, weak password)
            return Response({
                'detail': 'Invalid input.',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']
        try:
            # Decode the token to get user info
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
            user = User.objects.get(id=payload['id'], email=payload['email'])
        except jwt.ExpiredSignatureError:
            return Response({'detail': 'The reset link has expired. Please request a new one.'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({'detail': 'Invalid reset token. Please use the link from your email.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'detail': 'User not found for this reset token.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Catch-all for unexpected errors
            return Response({'detail': f'Unexpected error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            # Set the new password securely
            user.set_password(new_password)
            user.token = ''  # Invalidate the token after use
            user.save()
        except Exception as e:
            return Response({'detail': f'Failed to reset password: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)
