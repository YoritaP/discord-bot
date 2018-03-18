import discord
import function.bitcoin_init

#get bitcoin balance
def debug(client, message):
    print("called : debug")

    responce = discord.Embed(title='Debug', colour=0xDEADBF)
    responce.add_field(name="user : ", value=message.author.name, inline=False)
    return responce

def getMessageMining():
    rpc = function.bitcoin_init.bitcoin_init()

    tx = rpc.generate(1)
    print("MSG : " + tx[0])
