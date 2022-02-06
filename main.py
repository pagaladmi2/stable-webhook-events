import discord
from discord.ext import commands

client = commands.Bot(command_prefix="+++", self_bot=True)

## Above part is formality, the code you're looking from starts from here
webhook_spam = False 

TOKEN = "Your token here"

@client.command()
async def start():
  global webhook_spam
  webhook_spam = True

@client.command()
async def stop():
  global webhook_spam
  webhook_spam = False


@client.event
async def on_guild_channel_create(channel):
    while webhook_spam:                                                 ##You can replace this with an "if" statement 
        try:                                                            ##Enter your code for the webhook spam between the try and except: statement.
            for i in range(350):                                        ##you can make this an infinite loop by removing this
                webhook = await channel.create_webhook(name="Hi")
            while True: 
                await webhook.send("Test.")
        except:
         print("Webhook event isn't on.")
 

client.run(TOKEN, bot=False)
