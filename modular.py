import discord
import asyncio
import pathlib
from coms import *
import time
import requests
from PIL import Image

client = discord.Client()



commands = {}

def loadcommands():
    curdir = pathlib.Path('./coms')

    for command in curdir.iterdir():
        if command.name[0] != "_" and command.name[0] != ".":
            com = globals()[command.name[:-3]]

            comobj = com.Com()

            for key in comobj.keys:
                if key in commands:
                    commands[key].append(comobj)
                else:
                    commands[key] = [comobj]


loadcommands()

async def handle(message, original):
    if message.author == client.user:
        return

    for command in commands.keys():
        if command == "*" or (message.content.startswith(command) and original):
            for com in commands[command]:
                await com.main(client, message)
                if command != "*":
                    break


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    await handle(message, True)

@client.event
async def on_message_edit(before, after):
    await handle(after, False)

@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    message = await client.get_channel(payload.channel_id).get_message(payload.message_id)
    user = guild.get_member(payload.user_id)
    emoji = payload.emoji.name
    perms = [":)", "Moderator", "Moderator-In-Training"]
    
    for role in user.roles:
        if role.name in perms:
            if emoji == "👌":
                fil = message.attachments[0]
                channel = client.get_channel(519563109300568074)
                img = Image.open(requests.get(fil.url, stream=True).raw)
                img.save("./assets/halloffame.png")
                await channel.send(message.author.mention)
                await channel.send(file=discord.File("./assets/halloffame.png"))

@client.event
async def on_member_join(member):
    if member.guild.name == "mcskewl\'s locker room club":
        serverchannel = client.get_channel(457004484011491329)
        msg = "ey, welcome to the server " + member.mention + "! good luck lol"
        await serverchannel.send(msg)

        role = discord.utils.get(member.guild.roles,name="Memeboys")

        await member.add_roles(role)


client.run('NDc4MzI2NzYxMzE5NDMyMjI3.DuhI4Q.uNoTbK07TqDUGJdDRESB2MI-yEY')

