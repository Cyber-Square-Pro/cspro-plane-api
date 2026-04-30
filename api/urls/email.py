from django.urls import path
from api.views.email import EmailTestView

urlpatterns = [
    path("email-test/", EmailTestView.as_view()),
]
