from django.test import TestCase

from db.models import User, Workspace


class WorkspaceModelTests(TestCase):
    def test_workspace_string_representation_returns_name(self):
        # Unit test: verify Workspace model string behavior.
        user = User.objects.create_user(
            email="owner@example.com",
            username="owner-user",
            password="test-password",
        )
        workspace = Workspace.objects.create(
            name="Cyber Square",
            slug="cyber-square",
            organization_size="1-10",
            owner=user,
        )

        self.assertEqual(str(workspace), "Cyber Square")
