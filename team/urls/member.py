from team.views import MemberEndPoint
from django.urls import path

urlpatterns = [
    path('member/', MemberEndPoint().as_view()),
]