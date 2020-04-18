import asyncio
import json
from cse312.users.models import User
from .models import Post, Comments
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

class PostConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected", event)
        await self.send({
            "type":"websocket.accept"
        })

    async def websocket_receive(self, event):
        print("Received", event)

    async def websocket_disconnect(self, event):
        print("Disconnected", event)