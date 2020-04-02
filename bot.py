import os

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    servers=list(client.guilds)
    members=list(client.guilds[0].members)
    textChannels=list(client.guilds[0].text_channels)
    
    print(textChannels[1].id)
   
    for i in range(len(textChannels)): #send message to everyone
      channelId = client.get_channel(textChannels[i].id)
      await channelId.send('Test Message @everyone')

    # print(channels)
# @client.event
# async def report(server, name, *args, **kwargs):
#     channel = discord.utils.get(server.channels, name=name, type=discord.ChannelType.text)
#     print(channel)

    # for x in range(len(members)): //members
    # 	print(members[x-1])
    # for x in range(len(servers)):
    #  print(''+servers[x-1].name)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

   

#     if message.content == 'Test Jer':
#         response = "Tangina niyong lahat mga bobo @everyone"
#         await message.channel.send(response)

@client.event
async def on_member_join(member): 
    print(f'Welcome {member}')


@client.event
async def on_member_remove(member): 
    print(f'{member}has left')


client.run(TOKEN)