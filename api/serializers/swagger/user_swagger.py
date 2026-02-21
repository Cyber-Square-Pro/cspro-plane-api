from rest_framework import serializers


class CustomUserRetrievalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    avatar = serializers.ImageField()
    cover_image = serializers.ImageField()
    date_joined = serializers.DateTimeField()
    display_name = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_active = serializers.BooleanField()
    is_bot = serializers.BooleanField()
    is_email_verified = serializers.BooleanField()
    is_managed = serializers.BooleanField()
    is_onboarded = serializers.BooleanField()
    is_tour_completed = serializers.BooleanField()
    mobile_number = serializers.CharField()
    role = serializers.CharField()
    onboarding_step = serializers.JSONField()
    user_timezone = serializers.CharField()
    username = serializers.CharField()
    theme = serializers.CharField()
    last_workspace_id = serializers.IntegerField()
    
class UserMeSettingsSwaggerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    workspace = serializers.CharField()


class UserMeUpdateSerializer(serializers.Serializer):
    display_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    mobile_number = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    onboarding_step = serializers.JSONField(required=False)
    user_timezone = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    theme = serializers.CharField(required=False)
    last_workspace_id = serializers.IntegerField(required=False)

class EmailVerifyInputSerializer(serializers.Serializer):
    otp = serializers.CharField()

class EmailVerifyOutputSerializer(serializers.Serializer):
    statusCode = serializers.IntegerField()
    message = serializers.CharField()


