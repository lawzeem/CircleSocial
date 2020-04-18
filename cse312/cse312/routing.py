from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from cse312.feed.consumer import PostConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url('', PostConsumer, name='showFeed'),
                ]
            )
        )
    )
})