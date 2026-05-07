from django.test import TestCase
from rest_framework.test import APIClient


class SignUpApiTests(TestCase):
    def test_user_can_sign_up(self):
        # API test: exercise the real signup endpoint through DRF's client.
        client = APIClient()

        response = client.post(
            "/api/user/sign-up/",
            {
                "email": "new-user@example.com",
                "password": "strong-test-password",
            },
            format="json",
            HTTP_USER_AGENT="api-test-client",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["statusCode"], 201)
        self.assertEqual(response.data["message"], "Hey! Account Created")
        self.assertIn("accessToken", response.data)
        self.assertIn("refreshToken", response.data)
