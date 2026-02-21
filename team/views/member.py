from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.views import APIView

class MemberEndPoint(APIView):

    def get(self, request):

        """
        Author: Sreethu on 17th July 2024
        Purpose: Add member to team.
        Input parameters:  
        Return: 

        """

        return HttpResponse('Add new member')