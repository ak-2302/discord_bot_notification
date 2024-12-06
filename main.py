import discord
from config import Config
from dice import Dice

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

config = Config()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}.")
    return


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    return_channel = message.channel
    return_message = Dice(message.content).output
    if return_message != "":
        await return_channel.send(return_message)
    return


@client.event
async def on_member_join(member):
    return


client.run(token)

with open("token", "r", encoding="utf-8") as f:
    token = f.read()
client.run(token)
