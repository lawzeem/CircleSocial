import asyncio
import json
from cse312.users.models import User
from .models import Post, Comments
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
#
# class PostConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("Connected", event)
#         post = await database_sync_to_async(self.get_post)()
#         print("Post : ", post)
#         await self.send({
#             "type":"websocket.accept",
#             "posts":post
#         })
#
#     async def websocket_receive(self, event):
#         print("Received", event)
#
#     async def websocket_disconnect(self, event):
#         print("Disconnected", event)
#
#     def get_post(self):
#         return list(Post.objects.all())

class CommentConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected", event)
        post_id = self.scope['url_route']['kwargs']['post_id']
        post_group = f"Comments_{post_id}"
        self.post_group = post_group
        await self.channel_layer.group_add(
            post_group,
            self.channel_name
        )
        await self.send({
            "type":"websocket.accept",
            "text":"comments[0].comment"
        })

    async def websocket_receive(self, event):
        comment = event.get('text')
        user = self.scope['user']
        post_id = self.scope['url_route']['kwargs']['post_id']
        post = await self.get_post(post_id)
        print("Username: ", user.user_name)
        print("Message", event)
        await self.make_comment(post, user, comment)
        response = {
            "username": user.user_name,
            "comment": comment
        }
        new_event = {
            "type":"websocket.send",
            "text":comment
        }
        await self.channel_layer.group_send(
            self.post_group,
            {
                "type":"post_comment",
                "text":json.dumps(response)
            }
        )

    async def post_comment(self, event):
        print("Messsage", event)
        await self.send({
            "type":"websocket.send",
            "text":event['text']
        })

    async def websocket_disconnect(self, event):
        print("Disconnected", event)

    @database_sync_to_async
    def get_post(self, post_id):
        post = Post.objects.get(id = post_id)
        print("Post: ", post)
        return post

    @database_sync_to_async
    def make_comment(self, post, user, comment):
        return Comments.objects.create(post=post, user=user, comment=comment)
