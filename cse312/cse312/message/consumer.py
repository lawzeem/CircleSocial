import asyncio
import json
from cse312.users.models import User
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Thread, ChatMessage

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("-------connected to messaage consumer",event)
        await self.send({
            "type":"websocket.accept"
        })
        chatWith = self.scope['url_route']['kwargs']['username']
        user = self.scope['user']
        messagesThread = await self.get_messages(user,chatWith)
        # await asyncio.sleep(30)

    @database_sync_to_async
    def get_messages(self, user, chatWith):
        messages = Message.objects.get_or_new(user,chatWith)[0]
        return message

    async def websocket_receive(self,event):
            # print("recieve",event)
            msgText = event.get('text',None)
            print("---------------Received : ", msgText)
            if msgText is not None:
                text = json.loads(msgText)
                messageText = text.get('message')
                await self.send({
                    "type":"websocket.send",
                    "text":messageText
                })

    async def websocket_disconnect(self,event):
        print("disconnected from messaage consumer",event)
