import discord
import os
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    if datetime.datetime.today().weekday()==2:
       await client.get_channel(266880999349026818).send('Salut les HKM, du monde ce soir ?');
       

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("ODU5NTM4MDgyNDQwOTM3NDcz.YNuJOA.QfUNDIixPdeEC_Wrbr4Sj7KSWzg")