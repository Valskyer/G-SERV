import discord

token = 'YOUR BOT TOKEN HERE'
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='A Movie'))

@client.event
async def on_member_join(member):
    guild = client.get_guild() # YOUR INTEGER GUILD ID HERE
    welcome_channel = guild.get_channel() # YOUR INTEGER CHANNEL ID HERE
    await welcome_channel.send(f'Welcome to the {guild.name} Discord Server, {member.mention} !  :partying_face:')
    await member.send(f'We are glad to have you in the {guild.name} Discord Server, {member.name} !  :partying_face:')

@client.event
async def on_message(message):
    if message.content == 'hi':
        await message.channel.send('Hello!')

client.run(token)
