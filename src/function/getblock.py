import discord

#get bitcoin block info
def getBlock(rpc, client, message):
    print("called : getBlock")
    tx = message.content[10:]
    print("tx : " + tx)
    block = rpc.getblock(tx)
    print(block)
    responce = discord.Embed(title=tx, colour=0xDEADBF)
 
    responce.add_field(name="confirmations : ", value=block["confirmations"], inline=True)
    responce.add_field(name="height : ", value=block["height"], inline=True)
    responce.add_field(name="difficulty : ", value=block["difficulty"], inline=True)
    responce.add_field(name="merkleroot : ", value=block["merkleroot"], inline=False)
    return responce
