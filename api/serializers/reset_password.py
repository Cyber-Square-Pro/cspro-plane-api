from rest_framework import serializers

# Serializer for handling password reset requests
# Requires the reset token and the new password
import re

class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=12, write_only=True)

    def validate_new_password(self, value):
        # Check minimum length
        if len(value) < 12:
            raise serializers.ValidationError("Password must be at least 12 characters long.")
        # Check for at least one uppercase letter
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        # Check for at least one special character
        if not re.search(r'[^A-Za-z0-9]', value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return value
