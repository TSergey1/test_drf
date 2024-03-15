from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.filters import EventFilter
from api.serializers import (EventSerializer,
                             OrganizationSerializer,
                             UserSerializer)
from api.tasks import save_event
from event.models import Event, Organization

User = get_user_model()


class EventViewSet(viewsets.ModelViewSet):
    """Вьюсет мероприятия"""
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = EventFilter
    ordering_fields = ('date')
    search_fields = ('title',)
    page_size_query_param = 'limit'

    def create(self, request):
        save_event.delay(request.data)
        return Response({'message': 'Мероприятие добавляется'},
                        status=status.HTTP_102_PROCESSING)


class OrganizationViewSet(viewsets.ModelViewSet):
    """Вьюсет организации"""
    queryset = Organization.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrganizationSerializer


class CreateUserViewSet(viewsets.ModelViewSet):
    """Вьюсет пользователя"""
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
