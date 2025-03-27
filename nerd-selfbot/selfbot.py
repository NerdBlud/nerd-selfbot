import discord

class SelfBotMixin:
    def __init__(self, *args, **kwargs):
        self._self_bot = True
        super().__init__(*args, **kwargs)
    
    def _check_intents(self):
        if self._self_bot:
            return {}  
        return super().intents

    def run(self, token):
        self._self_bot = True
        self._intents = self._check_intents() 
        super().run(token)
