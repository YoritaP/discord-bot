import discord

#get bitcoin balance
def getbalance(rpc, client, message):
    print("called : balance")
    
    address = rpc.getaddressesbyaccount(message.author.id)

    if address:
        balance = float(rpc.getbalance(message.author.id))
    else:
        address = rpc.getaccountaddress(message.author.id)
        balance = float(rpc.getbalance(message.author.id))
    print(balance)
    responce = discord.Embed(title='Bitcoin balance', colour=0xDEADBF)
    
    responce.add_field(name="user : ", value="<@" + message.author.id + ">", inline=False)
    responce.add_field(name="btc : ", value=balance, inline=False)
    return responce
