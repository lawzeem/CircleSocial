import asyncio
import json
from cse312.users.models import User
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async, async_to_sync

from .models import Thread, ChatMessage
from cse312.users.models import User

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
        # print("connection successful")
        # message = sync_to_async(self.get_messages)(thread)
        # print("---------------------------------------- message: ", message)
        # # await asyncio.sleep(30)

    @database_sync_to_async
    def get_messages(self, thread):
        message = ChatMessage.objects.filter(thread=thread)
        return message

    @database_sync_to_async
    def get_thread(self, user, chatWith):
        other_user = User.objects.get(user_name=chatWith)
        thread = Thread.objects.get_or_new(user, other_user)[0]
        # print("---------------------------------------- thread: ", thread)
        return thread

    async def websocket_receive(self,event):
        chatWith = self.scope['url_route']['kwargs']['username']
        user = self.scope['user']
        thread = await self.get_thread(user, chatWith)
        message = json.loads(event.get('text'))
        print("================== message: ", message)
            # msgText = event.get('text',None)
        # print("---------------Received : ", msgText)
        if message != "":
            await self.new_message(thread, message)

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
        user = user = self.scope['user']
        return ChatMessage.objects.create(thread = thread, user = user, message = message)


    async def websocket_disconnect(self,event):
        print("Disconnected",event)
