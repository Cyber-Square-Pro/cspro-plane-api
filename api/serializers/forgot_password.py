from rest_framework import serializers

# Serializer for handling forgot password requests
# Only requires the user's email
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
