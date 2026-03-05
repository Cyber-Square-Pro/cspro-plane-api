from .attendance import urlpatterns as attendance_urls
from .member import urlpatterns as member_urls
from .team import urlpatterns as team_urls


urlpatterns = [
    *attendance_urls,
    *member_urls,
    *team_urls
]