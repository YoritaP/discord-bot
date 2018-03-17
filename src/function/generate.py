import discord

#get bitcoin balance
def mining(rpc, client, message):
    print("called : generate")
    
    tx = rpc.generate(1)
    print(tx)

    responce = discord.Embed(title='Generate New Block', colour=0xDEADBF)
    
    responce.add_field(name="txid : ", value=tx, inline=False)
    return responce
