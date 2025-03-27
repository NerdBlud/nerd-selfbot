import discord
import asyncio
from .utils import log, rate_limit
from .selfbot import SelfBotMixin

class MyClient(SelfBotMixin, discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = None  
        self.command_prefix = ">"  
        self._event_handlers = {}  

    async def on_ready(self):
        log(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith(self.command_prefix):
            await self.handle_command(message)

    async def handle_command(self, message):
        command = message.content[1:].split()[0] 
        if command in self._event_handlers:
            await self._event_handlers[command](message)

    def add_event_handler(self, event, handler):
        self._event_handlers[event] = handler

    def run(self, token):
        self.token = token
        super().run(token)
