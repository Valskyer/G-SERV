import discord

token = 'YOUR_BOT_TOKEN_HERE'
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='A Movie'))

@client.event
async def on_member_join(member):
    guild = client.get_guild(790639847358464102) # YOUR INTEGER GUILD ID HERE
    welcome_channel = guild.get_channel(790639847970308098) # YOUR INTEGER CHANNEL ID HERE
    role = guild.get_role(790645252004118538) # YOUR INTEGER ROLE ID HERE
    await member.add_roles(role)
    await welcome_channel.send(f'Welcome to the {guild.name} Discord Server, {member.mention} !  :partying_face:')
    await member.send(f'We are glad to have you in the {guild.name} Discord Server, {member.name} !  :partying_face:')

@client.event
async def on_message(message):
    if message.content == 'hi':
        await message.channel.send('Hello!')

client.run(token)
