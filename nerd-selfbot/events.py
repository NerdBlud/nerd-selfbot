async def on_ready(client):
    print(f"Logged in as {client.user}")

async def on_message(client, message):
    if message.content == "ping":
        await message.channel.send("pong")
