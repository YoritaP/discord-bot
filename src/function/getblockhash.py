import discord
import re
import function.bitcoin_init

#get bitcoin block hash
def getBlockHash(client, message):
    print("called : getBlockHash")

    rpc = function.bitcoin_init.bitcoin_init()

    block_number = re.findall(r'([+-]?[0-9]+\.?[0-9]*)', message.content)[0]
    print("block number : " + str(block_number))
    block_hash = rpc.getblockhash(int(block_number))

    responce = discord.Embed(title='Block Hash', colour=0xDEADBF)
    
    responce.add_field(name="block : " + str(block_number), value=block_hash, inline=False)
    return responce
