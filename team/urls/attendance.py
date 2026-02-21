from team.views import AttendanceEndPoint
from django.urls import path

urlpatterns = [
    path('attendance/', AttendanceEndPoint().as_view()),
]