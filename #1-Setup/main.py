import discord

token = 'YOUR_BOT_TOKEN'
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Over This Server'))

@client.event
async def on_message(message):
    if message.content == 'hi':
        await message.channel.send('Hello!')

client.run(token)
