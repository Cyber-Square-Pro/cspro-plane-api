from rest_framework import serializers


class WorkspaceCheckInputSerializer(serializers.Serializer):
    workspace_slug = serializers.CharField()


class WorkspaceCreateSerializer(serializers.Serializer):
    workspace_name = serializers.CharField()
    slug = serializers.CharField()
    organization_size = serializers.CharField()



