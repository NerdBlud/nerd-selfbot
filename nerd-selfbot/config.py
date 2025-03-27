class Config:
    def __init__(self):
        self.prefix = "!"
        self.log_channel = None
        self._self_bot = True

    def set_token(self, token):
        self.token = token
