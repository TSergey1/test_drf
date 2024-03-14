from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import EventViewSet, OrganizationViewSet

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('events/',
         EventViewSet.as_view(actions={'post': 'create', 'get': 'list'}),
         name='event-create'),
    path('organizations/',
         OrganizationViewSet.as_view(actions={'post': 'create'}),
         name='organization-create'),
]
