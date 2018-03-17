import discord

#get bitcoin balance
def getbalance(rpc, client, message):
    print("called : balance")
    
    id = str(message.author.id)

    rpc.getaccountaddress(id)
    address = rpc.getaddressesbyaccount(id)[0]
    balance = float(rpc.getbalance(id))
    print(balance)
    responce = discord.Embed(title='Bitcoin balance', colour=0xDEADBF)
    
    responce.add_field(name="Address : ", value=address, inline=False)
    responce.add_field(name="user : ", value="<@" + id + ">", inline=True)
    responce.add_field(name="btc : ", value=balance, inline=True)
    return responce
