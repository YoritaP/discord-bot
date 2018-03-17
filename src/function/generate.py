import discord

#get bitcoin balance
def pre_mining(rpc, client, message):
    print("called : generate")
    
    tx = rpc.generate(101)

    responce = discord.Embed(title='Generate 100 Blocks', colour=0xDEADBF)
    
    responce.add_field(name="txid : ", value=tx[0], inline=False)
    responce.add_field(name="txid : ", value=tx[1], inline=False)
    responce.add_field(name="txid : ", value=tx[2], inline=False)
    responce.add_field(name="And +98 blocks : ", value="100 blocks generated!", inline=False)
    return responce

#generate 1 block
def mining(rpc, client, message):
    print("called : generate")
    
    tx = rpc.generate(1)
    print(tx[0])

    responce = discord.Embed(title='Generate New Block', colour=0xDEADBF)
    
    responce.add_field(name="txid : ", value=tx[0], inline=False)
    return responce
