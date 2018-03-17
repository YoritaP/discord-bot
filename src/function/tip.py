import discord


#get bitcoin balance
def faucet(rpc, client, message):
    print("called : tip:faucet")
    
    balance = rpc.getbalance("")
    print("Amount : " + str(balance))
    amount = balance / 100

    id = str(message.author.id)

    rpc.getaccountaddress(id)
    address = rpc.getaddressesbyaccount(id)[0]

    print(address)
    tx = rpc.sendtoaddress(address, amount)

    print(tx)
    responce = discord.Embed(title='Faucet', colour=0xDEADBF)
    responce.add_field(name="user : ", value="<@" + id + ">", inline=False)
    responce.add_field(name="amount : ", value=amount, inline=False)
    responce.add_field(name="txid : ", value=tx, inline=False)
    return responce