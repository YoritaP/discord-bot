import discord
import asyncio

#get bitcoin balance
def faucet(rpc, client, message):
    print("called : tip:faucet")
    
    balance = rpc.getbalance("")
    print("Amount : " + str(balance))
    amount = balance / 100

    id = str(message.author.id)

    address = rpc.getaddressesbyaccount(id)
    if address:
        address = address[0]
        balance = float(rpc.getbalance(id))
    else:
        rpc.getnewaddress(id)
        address = rpc.getaddressesbyaccount(id)
        address = address[0]

    print(address)
    tx = rpc.sendtoaddress(address, amount)

    print(tx)
    responce = discord.Embed(title='Faucet', colour=0xDEADBF)
    responce.add_field(name="user : ", value="<@" + id + ">", inline=False)
    responce.add_field(name="amount : ", value=amount, inline=False)
    responce.add_field(name="txid : ", value=tx, inline=False)
    return responce