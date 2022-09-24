import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

red = 0xff0000
green = 0x00ff00


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.bot:
            return

        link = "https://www.youtube.com/watch?v=_MwVuay1WD8"
        img = "https://user-images.githubusercontent.com/43940682/181638380-921e157d-15d2-46ab-abe6-189ce1795b9b.png"
        embedVar = discord.Embed(title="Title", description="Desc", color=green, url=link)
        embedVar.set_image(url=img)
        embedVar.set_thumbnail(url=img)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)
        print(f'Message from {message.author}: {message.content}')


client = MyClient(intents=discord.Intents.default())
client.run(TOKEN)
