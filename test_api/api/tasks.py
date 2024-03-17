import logging
from time import sleep

from api.serializers import EventSerializer
from celery import shared_task
from event.models import Event

logger = logging.getLogger(__name__)


@shared_task
def save_event(data: dict, *args, **kwargs):
    sleep(2)
    serializer = EventSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.create(serializer.validated_data)

@shared_task
def save_event(data: dict, *args, **kwargs):
    sleep(2)
    serializer = EventSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    Event.objects.create(**serializer.validated_data)
