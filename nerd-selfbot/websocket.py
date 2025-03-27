import websockets
import json

class WebSocketHandler:
    def __init__(self, token):
        self.token = token
        self.ws_url = "wss://gateway.discord.gg/?v=10&encoding=json"
        self.connection = None

    async def connect(self):
        self.connection = await websockets.connect(self.ws_url)

    async def receive_message(self):
        while True:
            msg = await self.connection.recv()
            self.handle_message(json.loads(msg))

    def handle_message(self, message):
        print("Received:", message)
