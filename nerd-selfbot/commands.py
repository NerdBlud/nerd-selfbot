from .client import MyClient

class CommandHandler:
    def __init__(self, client: MyClient):
        self.client = client

    def command(self, name):
        def decorator(func):
            self.client.add_event_handler(name, func)
            return func
        return decorator
