from rest_framework import serializers
from .base import BaseSerializer
from .workspace import WorkspaceLiteSerializer
from db.models import Project,ProjectMember

class ProjectSerializer(BaseSerializer):
    
    workspace_detail = WorkspaceLiteSerializer(source="workspace", read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = [
            "workspace",
        ]

    def create(self, validated_data):
        workspace_id = self.context.get("workspace_id")  # Get workspace_id from context
        validated_data["workspace_id"] = workspace_id  # Assign it before saving
        return Project.objects.create(**validated_data)

    def validate(self, data):
        """Check if project name already exists in the workspace."""
        workspace_id = self.context.get("workspace_id")
        project_name = data.get("project_name")

        if Project.objects.filter(project_name=project_name, workspace_id=workspace_id).exists():
            raise serializers.ValidationError({"name_taken": "Project name taken"})

        return data
    
class ProjectLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "project_name","description","cover_image"]
        