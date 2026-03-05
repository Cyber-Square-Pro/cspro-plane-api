from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from api.serializers import WorkspaceLiteSerializer, WorkSpaceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.swagger.common_swagger import CommonResponseSerializer
from api.serializers.swagger.user_swagger import CustomUserRetrievalSerializer, EmailVerifyInputSerializer
from api.serializers.swagger.workspace_swagger import WorkspaceCreateSerializer
from db.models import Workspace, WorkspaceMember
from rest_framework import status
from .base import BaseAPIView
from db.models import User
from django.db.models import (
    Prefetch,
    OuterRef,
    Func,
    F,
)
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from Plane.decorator import authorized

 
class WorkspaceEndpoint(viewsets.ViewSet, BaseAPIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
            operation_description="Checks workspace slug availabilty",
            responses={200: CommonResponseSerializer},
        )
    def fetch_workspace(self, request):

        """
        Author: Mohammed Rifad on 29th April 2024
        Purpose: Retrieves user workspaces.
        Input parameters: None
        Return: Returns {'id', 'created_by', 'updated_by', 'created_at',
                      'updated_at', 'owner'}

        """
        member_count = (
            WorkspaceMember.objects.filter(
                workspace=OuterRef("id"), member__is_bot=False
            )
            .order_by()
            .annotate(count=Func(F("id"), function="Count"))
            .values("count")
        )
        workspace = (
            (
                Workspace.objects.prefetch_related(
                    Prefetch("workspace_member", queryset=WorkspaceMember.objects.all())
                )
                .filter(
                    workspace_member__member=request.user.id,
                )
                .select_related("owner")
            )
            .annotate(total_members=member_count)
            
        )
        

        serializer = WorkSpaceSerializer(self.filter_queryset(workspace), many=True)
        return Response( serializer.data)
    
    @swagger_auto_schema(
        operation_description="Creates new workspace",
        request_body=WorkspaceCreateSerializer,   
        responses={200: CommonResponseSerializer},  
    )

    def create(self, request):

        """
        Author: Mohammed Rifad on 28th April 2024
        Purpose: Retrieves user workspaces.
        Input parameters: workspace_name, slug, organization_size
        Return: Returns message, statusCode

        """

        try:
            
            slug = request.data['slug']
            workspace_name = request.data['name']
            organization_size = request.data['organization_size']
            print(slug,'999999999')
            serializer = WorkSpaceSerializer(data=request.data)
            workspace_slug = Workspace.objects.filter(slug = slug).exists()
            if workspace_slug:
                return Response(
                    {'status_code': 409, 
                     'message': 'Workspace URL is already taken!'
                     }) 
             
            if not workspace_name or not slug:
                return Response(
                    {'message': "Both name and slug are required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            if len(workspace_name) > 80 or len(slug) > 48:
                return Response(
                    {'message': "The maximum length for name is 80 and for slug is 48"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            if serializer.is_valid():
                serializer.save(owner_id = request.user.id)
                workspace = WorkspaceMember.objects.create(
                    workspace_id=serializer.data["id"],
                    member_id=request.user.id,
                    role=20,
                    
                )
                
                user = User.objects.get(id = request.user.id)
                user.is_onboarded = True

                user.last_workspace_id = serializer.data["id"]
                user.onboarding_step['workspace_create'] = True
                user.save()

                return Response({
                    'data':serializer.data,
                    'message': 'Workspace Created Succesfully',
                    })
            else:
                print(serializer.errors)
                return Response({
                    'data':serializer.data,
                    'message': 'Form Error',
                    })
        except :
           return Response({
                    'data':serializer.data,
                    'message': 'Something Went Wrong',
                    })

    def update_workspace(self, request):
        current_workspace = Workspace.objects.get(
            id=request.data["id"]
        )
        print(request.data)
        serializer = WorkspaceLiteSerializer(
             current_workspace, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Workspace updated successfully",
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
         
class WorkSpaceAvailabilityCheckEndpoint(APIView):
    permission_classes = [IsAuthenticated] 

    """
        Author: Mohammed Rifad on 27th April 2024
        Purpose: Checks workspace availability.
        Input parameters: workspace_slug
        Return: Returns message, statusCode

    """

    @swagger_auto_schema(
        operation_description="Checks workspace slug availabilty",
        responses={200: CommonResponseSerializer},
    )
    def get(self, request):
        slug = request.GET.get("slug", False)

        if not slug or slug == "":
            return Response({
                'message': 'Workspace Slug is required',
                'statusCode': 400
                })
        
        workspace = Workspace.objects.filter(slug=slug).exists()
        return Response({
            'status':not workspace,
            'statusCode': 200
             })


