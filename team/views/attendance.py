from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.views import APIView

class AttendanceEndPoint(APIView):
    
    def post(self, request):

        """
        Author: Sreethu on 17th July 2024
        Purpose: Add attendance of a member.
        Input parameters:  
        Return: 

        """
        
        return HttpResponse('Add attendance')