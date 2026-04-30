from django.http import JsonResponse
from rest_framework.views import APIView
from utils.email import is_valid_email

# EmailTestView does a simple check of a valid email in the URL parameter.
class EmailTestView(APIView):
    def get(self, request):
        email = request.GET.get("email", "")

        if not email:
            return JsonResponse(
                {"error": "email query param required"},
                status=400
            )

        return JsonResponse({
            "email": email,
            "valid": is_valid_email(email)
        })