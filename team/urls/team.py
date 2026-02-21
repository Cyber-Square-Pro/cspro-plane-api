from team.views import TeamEndPoint
from django.urls import path

urlpatterns = [
    path('add/', TeamEndPoint().as_view()),
]