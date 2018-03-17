import discord

#get help command
def command(rpc, client, message):
    print("called : command")
    
    responce = discord.Embed(title='Command list', colour=0xDEADBF)
    responce.add_field(name="!command : ", value="Return Command List", inline=False)
    responce.add_field(name="!balance : ", value="Return Your Bitcoin balance", inline=False)
    responce.add_field(name="!faucet : ", value="Get Some Bitcoin", inline=False)
    responce.add_field(name="!mining : ", value="Generate New Block", inline=False)
    responce.add_field(name="!getBlockCount : ", value="Return Now Block Height", inline=False)
    responce.add_field(name="!getBlockHash [num] : ", value="Return Block hash", inline=False)
    responce.add_field(name="!getBlock [hash] : ", value="Return Block info", inline=False)
    return responce
