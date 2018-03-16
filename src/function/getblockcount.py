import discord
from initializetion import init

#get bitcoin block count
def getBlockCount(client):
    print("called : getBlockCount")
    print(init.rpc_connection)
    block_count = init.rpc_connection.getblockcount()
    
    responce = discord.Embed(title='getBlockCount', colour=0xDEADBF)
    responce.set_author(name=client.user.name, icon_url=client.user.default_avatar_url)
        
    responce.add_field(name="blocks :", value=block_count, inline=False)
    return responce
