from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from team.models import ProjectTeam
from team.serializers import ProjectTeamSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TeamEndPoint(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        """
        Author: Sreethu on 17th July 2024 /Modified by Risvana pv and Aflaha on 16th OCT 2024
        Purpose: Add new team
        Input parameters:  
        Return: message, statusCode

        """

        # TODO: need to add permission class

        
        team_name = request.data.get('team_name','').lower().strip()
        team_description  = request.data.get('team_description','').strip()

        if not team_name:
            return Response(
                    
                    
                {'message':'Team name is required',
                    'statuscode': 400
                 },
                    status=status.HTTP_400_BAD_REQUEST

            )
        if not team_description:
            return Response(
                    
                    
                {'message':'Team description is required',
                 'statuscode': 400
                 },
                    status=status.HTTP_400_BAD_REQUEST

            )
        

        if  ProjectTeam.objects.filter(team_name=team_name).exists():
            return Response(
                    {'message':'Team Name Exists',
                     'statusCode': 409
                     },
                     status=status.HTTP_409_CONFLICT
            )
        data = {
            'team_name': team_name,
            'team_description': team_description
        }
       
        serializer = ProjectTeamSerializer(data=data)

        if serializer.is_valid():
                serializer.save()
                

                return Response(
                    {'message': 'Team Saved Succesfully.',
                     'statusCode': 201
                     },
                     status=status.HTTP_201_CREATED
                )
            
        return Response(
                    {'message': 'Invalid data',
                     'statusCode': 400,
                     'errors':serializer.errors
                     },
                     status=status.HTTP_400_BAD_REQUEST
                )
