import asyncio
import json
from cse312.users.models import User
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async, async_to_sync

from .models import Thread, ChatMessage
from cse312.users.models import User

from cse312.notifications.views import get_all_logged_in_users
from cse312.notifications.models import Notifications

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected", event)
        chatWith = self.scope['url_route']['kwargs']['username']
        user = self.scope['user']
        thread = await self.get_thread(user, chatWith)
        thread_group = f"Thread_{thread.id}"
        self.thread_group = thread_group

        await self.channel_layer.group_add(
            thread_group,
            self.channel_name
        )
        await self.send({
            "type":"websocket.accept"
        })

    @database_sync_to_async
    def get_messages(self, thread):
        message = ChatMessage.objects.filter(thread=thread)
        return message

    @database_sync_to_async
    def get_thread(self, user, chatWith):
        other_user = User.objects.get(id=chatWith)
        thread = Thread.objects.get_or_new(user, other_user)[0]
        return thread

    async def websocket_receive(self,event):
        chatWith = self.scope['url_route']['kwargs']['username']
        user = self.scope['user']
        thread = await self.get_thread(user, chatWith)
        message = json.loads(event.get('text'))

        mg = ""
        if message != "":
            mg = await self.new_message(thread, message)

            active = await self.user_active(chatWith)

            if not active:
                await self.new_notification(chatWith, mg)

        response = {
            "msgType" : "Message",
            "sender" : user.user_name,
            "message" : message
        }
        await self.channel_layer.group_send(
            self.thread_group,
            {
                "type":"broadcast_message",
                "text":json.dumps(response)
            }
        )

    async def broadcast_message(self, event):
        print("Messsage", event)
        await self.send({
            "type":"websocket.send",
            "text":event['text']
        })

    @database_sync_to_async
    def new_message(self, thread, message):
        user = self.scope['user']
        return ChatMessage.objects.create(thread = thread, user = user, message = message)

    @database_sync_to_async
    def new_notification(self, user, message):
        user = User.objects.get(id=user)
        return Notifications.add(user, message.user, message)

    @database_sync_to_async
    def user_active(self, user):
        user = User.objects.get(id=user)
        users = get_all_logged_in_users()
        if user in users:
            return True
        else:
            return False

    async def websocket_disconnect(self,event):
        print("Disconnected",event)
        raise StopConsumer()
