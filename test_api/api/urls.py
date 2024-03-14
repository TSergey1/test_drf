from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import CreateUserViewSet, EventViewSet, OrganizationViewSet

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('events/',
         EventViewSet.as_view(actions={'post': 'create', 'get': 'list'}),
         name='event-create'),
    path('events/<pk>/',
         EventViewSet.as_view({'get': 'retrieve'}), name='event-detail'),
    path('organizations/',
         OrganizationViewSet.as_view(actions={'post': 'create'}),
         name='organization-create'),
    path('users/', CreateUserViewSet.as_view({'post': 'create'})),
    path('token/login/', TokenObtainPairView.as_view()),
    path('jwt/refresh/', TokenRefreshView.as_view()),
]
