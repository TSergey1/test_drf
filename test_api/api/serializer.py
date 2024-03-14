import base64
from django.core.files.base import ContentFile
from rest_framework import serializers

from events.models import Event, Organization


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class OrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор организации."""
    users = serializers.ModelSerializer(many=True,
                                        required=False,
                                        source='event.users')

    class Meta:
        model = Organization
        fields = ('title',
                  'all_address',
                  'description')


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор мероприятия."""
    organization = OrganizationSerializer(many=True, required=False)
    image = Base64ImageField(required=False)

    class Meta:
        model = Event
        fields = ('title',
                  'description',
                  'image',
                  'date',
                  'users',
                  'organization')
