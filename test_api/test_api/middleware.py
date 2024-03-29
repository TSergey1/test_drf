from asgiref.sync import sync_to_async
from channels.middleware import BaseMiddleware
from channels.security.websocket import WebsocketDenier
from django.conf import settings
from django.contrib.auth import get_user_model
from jwt import InvalidTokenError
from jwt import decode as jwt_decode

User = get_user_model()


class ChatMiddleware(BaseMiddleware):
    """Проверка аутентифицировации пользователя перед соеденением вебсокетов"""
    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])
        denier = WebsocketDenier()
        if b'authorization' in headers:
            try:
                token = headers[b"authorization"].decode("utf-8")
                decoded_data = jwt_decode(token, settings.SECRET_KEY)

                scope['user'] = await sync_to_async(User.objects.get)(
                    id=decoded_data['user_id'],
                )
                return await super().__call__(scope, receive, send)
            except (User.DoesNotExist, InvalidTokenError):
                pass
        return await denier(scope, receive, send)
