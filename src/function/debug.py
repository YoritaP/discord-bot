import discord

import discord
import asyncio

#get bitcoin balance
def debug(client, message):
    print("called : debug")

    responce = discord.Embed(title='Debug', colour=0xDEADBF)
    responce.add_field(name="user : ", value="<@" + message.author.id + ">", inline=False)
    return responce
