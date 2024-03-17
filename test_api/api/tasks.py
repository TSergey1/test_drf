from time import sleep

from api.serializers import EventSerializer
from celery import shared_task


@shared_task
def save_event(data: dict):
    sleep(60)
    serializer = EventSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.create(serializer.validated_data)
