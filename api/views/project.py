from .base import BaseAPIView
from rest_framework import viewsets
from db.models import Workspace, ProjectMember, State,Project
from rest_framework.permissions import IsAuthenticated
from api.serializers import ProjectSerializer, ProjectLiteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class ProjectEndpoint(viewsets.ViewSet, BaseAPIView):
    permission_classes = [IsAuthenticated]
    

    def create_project(self, request, slug):
        print(request.data)
        workspace = Workspace.objects.get(slug = slug)    
        print(request.data)
        serializer = ProjectSerializer(
                data={**request.data.dict()}, context={"workspace_id": workspace.id}
            )

        print(request.data)
        try:

            serializer.is_valid(raise_exception=True)
            serializer.save() 
           
            return Response(
                {
                    "message": "Project created successfully",
                    "statusCode": 201,
                    "project": serializer.data,
                },
                
            )

        except ValidationError as e:
            errors = e.detail   
            print(errors)
            if "name_taken" in errors:   
                return Response(
                    {"message": "Project name taken", "statusCode": 409,  },
                    
                )

            return Response(
                {"message": "Validation failed", "statusCode": 400, },
               
            )

        except Exception as e:
            print(e)
            return Response(
                {"message": "An unexpected error occurred", "statusCode": 500 },
                
            )
 
    def list(self, request, slug):
        workspace = Workspace.objects.get(slug=slug)   
        projects = Project.objects.filter(workspace=workspace)

        if not projects.exists():
            return Response(
                {
                    "message": "No projects found for this workspace",
                    "statusCode": 200,
                    "projects": [],
                },
                 
            ) 
        serializer = ProjectLiteSerializer(projects, many=True)

        return Response(
            {
                "message": "Projects retrieved successfully",
                "statusCode": 200,
                "projects": serializer.data,
            },
            
        )

    def project_details(self,request,project_id):
        try:
            project = Project.objects.get(id=project_id) # fetching project by id
            serializer = ProjectSerializer(project) # converting project instance to json
            return Response(
                {
                    "message": "Project details retrieved successfully",
                    "statusCode": 200,
                    "project": serializer.data,
                },
                
            )
        except Project.DoesNotExist:
            return Response(
                {"message": "Project not found", "statusCode": 404},
                
            )

 
