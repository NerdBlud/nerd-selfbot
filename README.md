# 🤓 Nerd-SelfBot

Welcome to **nerd-selfbot**, a custom Python library designed for creating Discord bots with enhanced features. This library is based on the functionality of `discord.py` but with custom enhancements and features suited for self-bots and general bot development.

## 🚀 Features

- **Enhanced Event Handling**: Improved event handling for events like `on_ready`, `on_message`, and more.
- **WebSocket Management**: Seamlessly handles WebSocket connections with built-in reconnection logic.
- **API Interactions**: Simplified interactions with the Discord API, including sending messages, getting user data, etc.
- **Custom Error Handling**: Gracefully handles exceptions with custom exceptions tailored to our library.

## ❓ FAQ
Q: How do I get my bot's token?

A: Go to the [Discord Developer Portal](https://discord.com/developers/applications), create an application, and under the "Bot" tab, you'll find your bot's token. Keep it safe!

Q: How do I get my user token?

A: Go to discord.com on your browser, and paste this code into your console:
```py
(
    webpackChunkdiscord_app.push(
        [
            [''],
            {},
            e => {
                m=[];
                for(let c in e.c)
                    m.push(e.c[c])
            }
        ]
    ),
    m
).find(
    m => m?.exports?.default?.getToken !== void 0
).exports.default.getToken()
```

Q: Can I use this for a normal Discord bot?

A: Yes! Although nerd-selfbot is tailored for self-bots, you can easily use it for a normal bot by following the example code and making minor adjustments.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more information.

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

