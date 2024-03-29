import base64

import phonenumbers
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from event.models import Event, Organization
from rest_framework import serializers

User = get_user_model()


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
                  'description',
                  'address',
                  'postcode',
                  'all_address',
                  'users')
        extra_kwargs = {
            'address': {'write_only': True, },
            'postcode': {'write_only': True, },
        }


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор мероприятия."""
    organization = OrganizationSerializer(many=True, required=False)
    image = Base64ImageField(required=False)
    date = serializers.DateTimeField(input_formats=['%d.%m.%Y %H:%M'])

    class Meta:
        model = Event
        fields = ('title',
                  'description',
                  'image',
                  'date',
                  'organization')


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер User."""
    organizations = OrganizationSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('email', 'phone', 'password', 'organizations')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data: dict):
        user = User.objects.create_user(**validated_data)
        return user

    def validate_telephone(self, value):
        if value is None:
            return value
        elif value[0] != '+':
            value = f'+{value}'
        telephone = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(telephone):
            raise serializers.ValidationError('Некорректный номер телефона')
        return value
