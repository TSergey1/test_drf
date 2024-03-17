import base64
from time import sleep

from django.core.files.base import ContentFile

from api.serializers import EventSerializer
from celery import shared_task
from event.models import Event


def base64_to_content_file(data: base64 | None) -> ContentFile:
    if data:
        format, imgstr = data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return data
    return None


@shared_task
def save_event(validated_data: dict):
    sleep(2)
    image = base64_to_content_file(validated_data.pop('image', None))
    validated_data['image'] = image
    Event.objects.create(**validated_data)
