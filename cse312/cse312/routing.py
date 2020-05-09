from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from cse312.feed.consumer import CommentConsumer, PostConsumer, UpvoteConsumer
from cse312.message.consumer import ChatConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^upvote/(?P<post_id>[\w.@+-]+)", UpvoteConsumer, name='upvotePost'),
                    url(r"^view/(?P<post_id>[\w.@+-]+)", CommentConsumer, name='viewPost'),
                    url('add', PostConsumer, name='makePost'),
                    url('following', PostConsumer, name='showFollowingFeed'),
                    url('', PostConsumer, name='showFeed'),
                    url(r"^messages/(?P<username>[\w.@+-]+)/$", ChatConsumer, name='viewMessage'),
                ]
            )
        )
    )
})
