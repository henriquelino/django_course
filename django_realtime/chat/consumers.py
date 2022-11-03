from channels.generic.websocket import AsyncWebsocketConsumer

import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # get in room
        await self.channel_layer.group_add(self.room_group_name,
                                           self.room_name)

        await self.accept()
        return

    async def disconnect(self, code):
        # get out of room
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)
        return

    async def receive(self, data):
        """receives a message from websocket"""

        text_data_json = json.loads(data)
        message = text_data_json['message']

        # send message to room
        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'message': message
        })

        return

    async def chat_message(self, event: dict):
        """receive a message from room"""
        message = event['message']
        # send message to the websocket
        await self.send(text_data=json.dumps({'message': message}))
        return
