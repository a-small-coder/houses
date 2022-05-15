"""
ASGI config for "Property Ads Processor" project.
It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django_asgi_app = get_asgi_application()

from components.common import ws_routes

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            ws_routes.urlpatterns
        )
    )
})
