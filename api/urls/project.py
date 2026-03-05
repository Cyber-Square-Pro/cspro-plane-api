from api.views import ProjectEndpoint
from django.urls import path

urlpatterns = [
    path('workspace/<slug>/projects/', ProjectEndpoint.as_view({
        'post': 'create_project',
        'get': 'list',
    })),

    path('workspace/projects/<int:project_id>/', ProjectEndpoint.as_view({
        'get': 'project_details',}))

        #http://127.0.0.1:8000/api/workspace/projects/1/

]