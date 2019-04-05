import discord
from discord.ext.commands import Bot
import random
import asyncio
import time

client = Bot(description="Ravioli", command_prefix="", pm_help = False)

@client.event
async def on_message(message):
	if (message.author.bot == True):
		return
	if message.content.startswith('<@563578496706936833'):
		msg = 'Ravioli! {0.author.mention}'.format(message)
		link = 'http://overtontoolkit.me/rav' + str(random.randrange(1, 20)) + ".jpg"
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, link)

client.run('NTYzNTc4NDk2NzA2OTM2ODMz.XKbYpg.mXR-2m0Anzt8-XVxb92m_eHbwew')