import discord

#get bitcoin balance
def faucet(rpc, client, message):
    print("called : tip:faucet")
    
    balance = rpc.getbalance("")
    amount = balance / 100

    address = rpc.getaddressesbyaccount(message.author.id)[0]
    if address == False:
        address = rpc.getaccountaddress(message.author.id)
    print(address)
    tx = rpc.sendtoaddress(address, amount)

    print(tx)
    responce = discord.Embed(title='Faucet', colour=0xDEADBF)
    responce.add_field(name="user : ", value="<@" + message.author.id + ">", inline=False)
    responce.add_field(name="amount : ", value=amount, inline=False)
    responce.add_field(name="txid : ", value=tx, inline=False)
    return responce
