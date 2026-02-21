from rest_framework import serializers
from team.models import ProjectTeam
from team.serializers import BaseSerializer

class ProjectTeamSerializer(BaseSerializer):

    class Meta:
        model = ProjectTeam
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "status",
        ]