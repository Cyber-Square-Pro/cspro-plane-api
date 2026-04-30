from .authentication import urlpatterns as authentication_urls
from .user import urlpatterns as user_urls
from .workspace import urlpatterns as workspace_urls
from .project import urlpatterns as project_urls
from.profile import urlpatterns as profile_urls
from .email import urlpatterns as email_test_urls

urlpatterns = [
    *authentication_urls,
    *user_urls,
    *workspace_urls,
    *project_urls,
    *profile_urls,
    *email_test_urls
]
