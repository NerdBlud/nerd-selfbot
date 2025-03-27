import aiohttp

class DiscordAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://discord.com/api/v10"
        self.headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json",
        }

    async def get_user(self, user_id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/users/{user_id}", headers=self.headers) as resp:
                return await resp.json()

    async def get_guild(self, guild_id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/guilds/{guild_id}", headers=self.headers) as resp:
                return await resp.json()

    async def get_channel(self, channel_id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/channels/{channel_id}", headers=self.headers) as resp:
                return await resp.json()
            
            async with session.get(f"{self.base_url}/channels/{channel_id}", headers=self.headers) as resp:
                return await resp.json()