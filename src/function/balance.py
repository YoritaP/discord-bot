import discord
import function.bitcoin_init

#get bitcoin balance
def getbalance(client, message):
    print("called : balance")
    
    rpc = function.bitcoin_init.bitcoin_init()

    id = str(message.author.id)

    address = rpc.getaddressesbyaccount(id)
    if address:
        address = address[0]
        balance = float(rpc.getbalance(id))
    else:
        rpc.getnewaddress(id)
        address = rpc.getaddressesbyaccount(id)
        address = address[0]
        balance = float(rpc.getbalance(id))

    print(balance)
    responce = discord.Embed(title='Bitcoin balance', colour=0xDEADBF)
    
    responce.add_field(name="Address : ", value=address, inline=False)
    responce.add_field(name="user : ", value=message.author.name, inline=True)
    responce.add_field(name="btc : ", value=balance, inline=True)
    return responce
