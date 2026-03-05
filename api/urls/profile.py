from api.views import ProfileEndPoint
from django.urls import path

urlpatterns = [
    path('user/profile/', ProfileEndPoint.as_view({
        'get': 'display_profile', 
        'put': 'update_user_profile' 
    })),
    
    path('user/profile/change-password/', ProfileEndPoint.as_view({
        'put': 'change_password',
    })),
    

]