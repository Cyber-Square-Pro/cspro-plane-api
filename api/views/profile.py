from .base import BaseAPIView
from rest_framework import viewsets
from db.models import User
from api.serializers  import ProfileSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

class ProfileEndPoint(viewsets.ViewSet, BaseAPIView):
    
    def display_profile(self,request):
        user = User.objects.get(id=request.user.id)
        serializer = ProfileSerializer(user)
        return Response(
            {
                "message": "Profile fetched successfully",
                "statusCode": 200,
                "data": serializer.data,
            }
        )

    def update_user_profile(self,request):
        user = User.objects.get(id=request.user.id)
        serializer = ProfileSerializer(user, data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Profile updated successfully",
                    "statusCode": 200,
                    "data": serializer.data,
                }
            )
        else:
            return Response(
                {
                    "message": "Validation failed",
                    "statusCode": 400,
                    "errors": serializer.errors,
                }
            )

         
    def change_password(self, request):
        
        """
        Purpose: Allows an authenticated user to change their password.

        This method checks if the provided current password matches
        the user's existing password, and if so, updates the password
        to the new one provided.

        Expected request data:
            - currentPassword (str): The user's current password.
            - newPassword (str): The new password to set.

        Returns:
            - 200 : If the password was successfully changed.
            - 400 : If required fields are missing or the current password is incorrect.
        """

        user = User.objects.get(id=request.user.id)
        old_password = request.data.get("currentPassword")
        new_password = request.data.get("newPassword")

        if not old_password or not new_password:
            return Response(
                {
                    "message": "Both current and new passwords are required.",
                    "statusCode": 400,
                },
            )
        
        if not check_password(old_password, user.password):
            print("Password mismatch")
            return Response(
                {
                    "message": "Old password is incorrect",
                    "statusCode": 400,
                }
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {
                "message": "Password changed successfully",
                "statusCode": 200,
            }
        )