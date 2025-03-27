# 🤓 Nerd-SelfBot

Welcome to **nerd-selfbot**, a custom Python library designed for creating Discord bots with enhanced features. This library is based on the functionality of `discord.py` but with custom enhancements and features suited for self-bots and general bot development.

## 🚀 Features

- **Enhanced Event Handling**: Improved event handling for events like `on_ready`, `on_message`, and more.
- **WebSocket Management**: Seamlessly handles WebSocket connections with built-in reconnection logic.
- **API Interactions**: Simplified interactions with the Discord API, including sending messages, getting user data, etc.
- **Custom Error Handling**: Gracefully handles exceptions with custom exceptions tailored to our library.

## 🛠️ Installation

To get started with this library, follow these steps:

- **Variant 1:**
1. Clone the repository:
   git clone https://github.com/nerdblud/nerd-selfbot.git
2. pip install -r requirements.txt

- **Variant 2:**
1. pip install nerd-selfbot

# ⚙️ Usage

After installation, you can start using nerd-selfbot to create your own self-bot. Here's a simple example of how to get started:
# Example Code:

```py
import nerd_selfbot
class MySelfBot(nerd_selfbot.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
    async def on_message(self, message):
        if message.author == self.user:
            return
client = MySelfBot()

client.run("YOUR_BOT_TOKEN")
```
