import asyncio
import json
from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer
from app.models import Message


class ChatConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		await self.send({
				'type':'websocket.accept',
			})

		#//
		await self.channel_layer.group_add(
				'chat',
				self.channel_name
			)
		#//

	async def websocket_receive(self,event):
		print('recieved: ', event)
		new_message = json.loads(event.get('text'))['message_text']
		await self.create_message(new_message)

#		await self.send({
#				'type':"websocket.send",
#				'text':new_message
#			})
		#//
		message = {
			'new_message': new_message,
		}

		await self.channel_layer.group_send(
				'chat',
				{
					'type': 'show_message',
					'text': json.dumps(message)
				}
			)
		#//



	@database_sync_to_async
	def create_message(self, new_message):
		Message.objects.create(content=new_message)
		message = Message.objects.all()
		if message.count() > 10:
			message[0].delete()

	#//
	async def show_message(self, event):
		await self.send({
				'type':'websocket.send',
				'text':event['text']
			})

	#//


	async def websocket_disconnect(self, event):
		print('disconnect')