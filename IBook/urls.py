from django.urls import path, include
from rest_framework.routers import DefaultRouter
from IBookApp.views import SignUpView, SignInView, ProjectViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    # Authentication endpoints
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/signin/', SignInView.as_view(), name='signin'),
    
   
    path('api/', include(router.urls)),
]
