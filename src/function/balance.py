import discord

#get bitcoin balance
def getbalance(rpc, client, message):
    print("called : balance")
    
    rpc.getaccountaddress(message.author.id)
    address = rpc.getaddressesbyaccount(message.author.id)[0]
    balance = float(rpc.getbalance(message.author.id))
    print(balance)
    responce = discord.Embed(title='Bitcoin balance', colour=0xDEADBF)
    
    responce.add_field(name="Address : ", value=address, inline=False)
    responce.add_field(name="user : ", value="<@" + message.author.id + ">", inline=True)
    responce.add_field(name="btc : ", value=balance, inline=True)
    return responce
