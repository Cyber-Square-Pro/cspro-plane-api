from rest_framework import serializers


class CommonResponseSerializer(serializers.Serializer):
    statusCode = serializers.IntegerField()
    message = serializers.CharField()