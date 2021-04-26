import os
from dotenv import load_dotenv
import discord.ext.commands


load_dotenv()
client = discord.Client()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        'we have logged in as {0.user}'.format(client),
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello')

print(TOKEN)
client.run(TOKEN)
