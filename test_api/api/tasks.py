from time import sleep

from celery import shared_task

from api.serializers import EventSerializer


@shared_task
def save_event(data: dict, *args, **kwargs):
    sleep(2)
    serializer = EventSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.create(serializer.validated_data)
